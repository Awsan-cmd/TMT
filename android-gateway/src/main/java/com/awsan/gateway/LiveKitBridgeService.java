package com.awsan.gateway;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import androidx.annotation.Nullable;

public class LiveKitBridgeService extends Service {
    private static final String LIVEKIT_URL = "ws://192.168.1.103:7880";

    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        // تهيئة اتصال LiveKit باستخدام العنوان ws://192.168.1.103:7880 وتوجيه الصوت هنا
        return START_STICKY;
    }
}
