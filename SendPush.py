import FCMManager as fcm

tokens = ["edJItxgYQvyuyOxFHlMXhk:APA91bEpHQAlf51lp4xZsBblz"
          "-_PBzmM3g0kWpV-Zf8FhBib7ww2P_ZI8FA2R-dXUB2Vj6wRy7rd7uKY1_6Tt4XxKZcYqGDq6HhuQW4yXFxF_uMKU1eYrv-dlS51u0dQDfBKcFUHiryx"]
fcm.sendPush("Hi", "This is my next msg", tokens)
