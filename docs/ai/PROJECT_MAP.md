# خريطة مكونات AwsanBot (Project Map)

## هيكل الملفات والمكونات
- **Frontend / UI**: `public/index.html` (لوحة التحكم الموحدة).
- **Voice AI Agent**: `agent.py` (وكيل LiveKit والربط مع OpenAI و n8n).
- **Android Gateway**: 
  - `android-gateway/build.gradle`
  - `android-gateway/src/main/java/com/awsan/gateway/CallReceiver.java`
  - `android-gateway/src/main/java/com/awsan/gateway/LiveKitBridgeService.java`
  - Gradle wrapper (`gradlew`, `gradlew.bat`, `gradle/wrapper/gradle-wrapper.properties`).
- **Infrastructure / DevOps**:
  - `docker-compose.yml` (LiveKit & n8n)
  - `.github/workflows/build-apk.yml` (CI/CD build action)
- **Memory & Documentation**: `docs/ai/` و `AGENTS.md`.
