[app]

title = JARVIS
package.name = jarvis
package.domain = com.aditya

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy,charset-normalizer==3.4.3

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,RECORD_AUDIO
android.accept_sdk_license = True
android.archs = arm64-v8a,armeabi-v7a

[buildozer]

log_level = 2
warn_on_root = 1
