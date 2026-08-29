package com.awsan.gateway;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.telephony.TelephonyManager;
import okhttp3.*;
import java.io.IOException;

public class CallReceiver extends BroadcastReceiver {
    private final OkHttpClient client = new OkHttpClient();

    @Override
    public void onReceive(Context context, Intent intent) {
        if (intent.getAction() != null && intent.getAction().equals(TelephonyManager.ACTION_PHONE_STATE_CHANGED)) {
            String state = intent.getStringExtra(TelephonyManager.EXTRA_STATE);
            String number = intent.getStringExtra(TelephonyManager.EXTRA_INCOMING_NUMBER);

            if (TelephonyManager.EXTRA_STATE_RINGING.equals(state)) {
                sendWebhook(number, "RINGING");
                Intent serviceIntent = new Intent(context, LiveKitBridgeService.class);
                context.startService(serviceIntent);
            }
        }
    }

    private void sendWebhook(String number, String state) {
        MediaType JSON = MediaType.parse("application/json; charset=utf-8");
        String json = "{\"number\":\"" + (number != null ? number : "unknown") + "\",\"state\":\"" + state + "\"}";
        RequestBody body = RequestBody.create(JSON, json);
        Request request = new Request.Builder()
                .url("http://192.168.1.103:5678/webhook/call-events")
                .post(body)
                .build();

        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                e.printStackTrace();
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                response.close();
            }
        });
    }
}
