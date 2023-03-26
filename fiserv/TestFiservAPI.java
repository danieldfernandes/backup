package com.paywithmybank.server.v1.test.api.fiserv;

import org.json.JSONArray;
import org.json.JSONObject;
import org.junit.Assert;
import org.junit.Test;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class TestFiservAPI {

    @Test
    public void test_FI_Infos_Listcase_1() throws Exception {
        // Set the endpoint
        URL url = new URL("https://websrviqa.wm.cashedge.com/WealthManagementWeb/ws/" + "SeedDataInq/getFinancialInstInfo");

        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod("POST"); // request method
        con.setRequestProperty("Content-Type", "application/json"); // header
        con.setDoOutput(true);

        String requestBody = "{\n"
                             + "    \"RqUID\": \"RqUID0\",\n"
                             + "    \"SignonRq\": {\n"
                             + "        \"UserInfo\": {\n"
                             + "            \"UserID\": \"XMLAdminlcmpdz\",\n"
                             + "            \"HomeID\": 51090001,\n"
                             + "            \"UserPassword\": {\n"
                             + "                \"CryptType\": \"None\",\n"
                             + "                \"CryptVal\": \"Fiserv01$\"\n"
                             + "            },\n"
                             + "            \"Role\": \"Admin\"\n"
                             + "        }\n"
                             + "    },\n"
                             + "    \"FIInfoRq\": {\n"
                             + "        \"FIInfoRequired\": \"FIIDInfo\"\n"
                             + "    },\n"
                             + "    \"partnerID\": 51090000,\n"
                             + "    \"version\": \"version1\"\n"
                             + "}";

        // Writes request body in the connection output
        DataOutputStream wr = new DataOutputStream(con.getOutputStream());
        wr.writeBytes(requestBody);
        wr.flush();
        wr.close();

        // read API response
        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuffer response = new StringBuffer();
        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();
        //System.out.println(response.toString()); // print API response
        
        Assert.assertEquals("Expected status code 200, but found " + String.valueOf(con.getResponseCode()), 200, con.getResponseCode());

        JSONObject jsonResponse = new JSONObject(response.toString());
        JSONObject statusObj = jsonResponse.getJSONObject("Status");
        String statusDesc_Status = statusObj.getString("StatusDesc");
        Assert.assertEquals("Expected \'Success\', but found \'" + statusDesc_Status + "\'", "Success", statusDesc_Status);

        JSONObject signonRsObj = jsonResponse.getJSONObject("SignonRs");
        JSONObject statusSignonRsObj = signonRsObj.getJSONObject("Status");
        String statusDesc_Status_SignonRs = statusSignonRsObj.getString("StatusDesc");
        Assert.assertEquals("Expected \'Success\', but found \'" + statusDesc_Status_SignonRs + "\'", "Success", statusDesc_Status_SignonRs);

        JSONObject FIInfoRsObj = jsonResponse.getJSONObject("FIInfoRs");
        JSONObject statusFIInfoRsObj = FIInfoRsObj.getJSONObject("Status");
        String statusDesc_Status_FIInfoRs = statusFIInfoRsObj.getString("StatusDesc");
        Assert.assertEquals("Expected \'Success\', but found \'" + statusDesc_Status_FIInfoRs + "\'", "Success", statusDesc_Status_FIInfoRs);

        JSONObject fiIdListFIInfoRsObj = FIInfoRsObj.getJSONObject("FIIdList");
        JSONArray fiId_fiIdList_FIInfoRs = fiIdListFIInfoRsObj.getJSONArray("FIId");
        Assert.assertEquals("Expected 1500 FIs, but found " + String.valueOf(fiId_fiIdList_FIInfoRs.length()), 1500, fiId_fiIdList_FIInfoRs.length());
    }

    
    
    // public static void main(String[] args) {
    //     Result result = JUnitCore.runClasses(TestAPIFIServ.class);
    //     for (Failure failure : result.getFailures()) {
    //         System.out.println(failure.toString());
    //     }
    //     System.out.println("All tests passed");
    // }
}