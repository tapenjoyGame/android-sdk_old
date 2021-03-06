#! /usr/bin/python
# -*- coding:utf-8 -*-
'''
# Filename      : ./android-sdk/rules_pokemon.py
# Description   :
# Last modified : 2016-03-21 10:28
'''
# coding: utf-8
import os
from processor import register, Rule


class RuleBase(Rule):
    VERSION_CODE = '100000'
    VERSION_NAME = '1.00000'
    APPNAME = '神奇小精灵加强版'
    APPLABEL = 'pokemon'
    ICON_PATH = '../../../pokemon_icons/android'
    UMENG_APPKEY = '5682058be0f55a0ec8003010'
    CHANNEL_ID = 'empty'

    BASE_SDK_VERSION = """
    <uses-sdk android:minSdkVersion="8" android:targetSdkVersion="18"/>
    """

    BASE_PERMISSION = """
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.WAKE_LOCK" />
    <uses-permission android:name="android.permission.READ_LOGS" />
    <uses-permission android:name="android.permission.DUMP" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.GET_TASKS" />
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
    """

    NATIVE_MAIN_BOOT = True
    BASE_ACTIVITY = """
        <activity android:name="org.weilan.poem"
                  android:label="@string/app_name"
                  android:screenOrientation="portrait"
                  android:theme="@android:style/Theme.NoTitleBar.Fullscreen"
                  android:configChanges="keyboard|fontScale|keyboardHidden|orientation|screenSize|layoutDirection">
        """ + ("" if not NATIVE_MAIN_BOOT else """
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        """) + """
        </activity>

        <activity android:name="org.weilan.VideoActivity"
            android:label="@string/app_name"
            android:screenOrientation="portrait"
            android:configChanges="keyboardHidden|orientation|screenSize|layoutDirection">
            >
            <intent-filter>
                <action android:name="org.weilan.VideoActivity" />
                <category android:name="android.intent.category.DEFAULT"/>
            </intent-filter>
        </activity>

        <receiver android:name="org.weilan.PushReceiver" >
            <intent-filter android:priority="2147483647" >
                <action android:name="android.intent.action.BOOT_COMPLETED"/>
                <category android:name="android.intent.category.DEFAULT" />
                <action android:name="android.intent.action.USER_PRESENT"/>
            </intent-filter>
        </receiver>

        <service
            android:name="org.weilan.PushService"
            android:enabled="true"
            />
    """


@register
class RuleEmpty(RuleBase):
    LABEL = 'empty'
    DIRECTORY = 'empty'
    CH_NAME = '神奇小精灵加强版'
    SDKTYPE = '0'
    PACKAGE_NAME = 'com.winnergame.pokemon.empty'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.empty'
    CHANNEL_ID = 'empty'

@register
class RuleEmptyB(RuleBase):
    LABEL = 'emptyB'
    DIRECTORY = 'empty'
    CH_NAME = '神奇小精灵加强版-商务版'
    SDKTYPE = '0'
    PACKAGE_NAME = 'com.winnergame.pokemon.empty'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.empty'
    CHANNEL_ID = 'emptyB'

@register
class RuleUC(RuleBase):
    LABEL = 'uc'
    DIRECTORY = 'uc'
    CH_NAME = 'UC小包'
    SDKTYPE = '7'
    PACKAGE_NAME = 'com.winnergame.pokemon.uc'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.uc'
    CHANNEL_ID = 'uc'

    ICON_PATH = '../../../pokemon_icons/uc'

    GAMEID = '579041'

    @classmethod
    def rules(cls):
        return super(RuleUC, cls).rules() + [
            ('src/com/ninegame/ucgamesdk/UCSdkConfig.java', 'replace', cls.common_replaces()),
        ]


@register
class RuleC360(RuleBase):
    LABEL = 'c360'
    DIRECTORY = 'c360'
    CH_NAME = '360小包'
    SDKTYPE = '19'
    PACKAGE_NAME = 'com.winnergame.pokemonpro.qh360'
    YY_PACKAGE_NAME = 'com.winnergame.pokemonpro.qh360'
    CHANNEL_ID = 'qh360'

    # 多次搞错这个值了 ！！！！！！ QHOPENSDK_PRIVATEKEY = md5( appSecret + "#" + appKey )

    QHOPENSDK_APPKEY = '5bb2fd12276a01229263f167f7f3dd59'
    QHOPENSDK_PRIVATEKEY = 'e2773cf5dbdb829276ea0404d18b58a2'
    QHOPENSDK_APPID = '202887981'

    PAY_URL = 'http://pokemonpro.sdk.dnastdio.com:8888/sdk/c360/pay_callback'


@register
class RuleBaidu(RuleBase):
    LABEL = 'baidu'
    DIRECTORY = 'baidu'
    CH_NAME = '百度小包'
    SDKTYPE = '17'
    PACKAGE_NAME = 'com.winnergame.pokemon.baidu'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.baidu'
    CHANNEL_ID = 'baidu'

    ICON_PATH = '../../../pokemon_icons/baidu'

    APPID = '7187701'
    APPKEY = 'cmDV5PRTiFk4lrlydnsw3Dew'


@register
class RuleXiaomi(RuleBase):
    LABEL = 'xiaomi'
    DIRECTORY = 'xiaomi'
    CH_NAME = '小米小包'
    SDKTYPE = '18'
    PACKAGE_NAME = 'com.winnergame.pokemonpro.mi'
    YY_PACKAGE_NAME = 'com.winnergame.pokemonpro.mi'
    CHANNEL_ID = 'xiaomi'

    APPID = '2882303761517427343'
    APPKEY = '5881742752343'

    @classmethod
    def rules(cls):
        return super(RuleXiaomi, cls).rules() + [
            ('src/org/weilan/MiAppApplication.java', 'replace', cls.common_replaces()),
        ]


@register
class RuleWDJ(RuleBase):
    LABEL = 'wdj'
    DIRECTORY = 'wdj'
    CH_NAME = '豌豆荚小包'
    SDKTYPE = '22'
    PACKAGE_NAME = 'com.winnergame.pokemon.wdj'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.wdj'
    CHANNEL_ID = 'wdj'

    APPKEY = '100034487'
    SECURITY_KEY = 'e41c62ee82d9777bff71cabe0b1eb7a7'

    @classmethod
    def rules(cls):
        return super(RuleWDJ, cls).rules() + [
            ('src/org/weilan/sdk_app.java', 'replace', cls.common_replaces()),
        ]


@register
class RuleAnzhi(RuleBase):
    LABEL = 'anzhi'
    DIRECTORY = 'anzhi'
    CH_NAME = '安智小包'
    SDKTYPE = '21'
    PACKAGE_NAME = 'com.winnergame.pokemon.anzhi'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.anzhi'
    CHANNEL_ID = 'anzhi'

    ICON_PATH = '../../../pokemon_icons/anzhi'

    APPKEY = '14482459076Q40C2DSvGMJ2Y69551d'
    APPSECRET = 'F4TWgtKHesIKN5v3eEsSQM42'

    @classmethod
    def rules(cls):
        return super(RuleAnzhi, cls).rules() + [
            ('src/org/weilan/SplashActivity.java', 'replace', cls.common_replaces()),
        ]


@register
class RuleOppo(RuleBase):
    LABEL = 'oppo'
    DIRECTORY = 'oppo'
    CH_NAME = 'OPPO小包'
    SDKTYPE = '20'
    PACKAGE_NAME = 'com.winnergame.pokemon.nearme.gamecenter'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.oppo'
    CHANNEL_ID = 'oppo'

    APPID = '4671'
    APPKEY = 'bjiQLpsqyu8Gg4kgK8goCKko4'
    APPSECRET = '8d68A258e9D93812b86B532567635352'

    PAY_URL = 'http://pokemonpro.sdk.dnastdio.com:8888/sdk/oppo/pay_callback'


@register
class RuleYYH(RuleBase):
    LABEL = 'yyh'
    DIRECTORY = 'yyh'
    CH_NAME = '应用汇小包'
    SDKTYPE = '34'
    PACKAGE_NAME = 'com.winnergame.pokemon.yyh'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.yyh'
    CHANNEL_ID = 'yyh'

    APPID = '10932'
    APPKEY = 'xBtsAo9c4F1CNnW0'
    PAYID = '5000372262'
    PAYKEY = 'NTI0QzA3RURDNzVGM0JGOThGNUU5N0ZDNzQ1RDdDQzM5MEI5OTVBOU1USXlOek15TkRreE16WTNOakUxTmpRd01qTXJNak15TXpNeE5EYzJPVFEyTXpBNE5qUXpNalkyT1RjM05Ua3dOREE0TmpJek1USTVOek01'


@register
class RuleGfan(RuleBase):
    LABEL = 'gfan'
    DIRECTORY = 'gfan'
    CH_NAME = '机锋小包'
    SDKTYPE = '28'
    PACKAGE_NAME = 'com.winnergame.pokemon.gfan'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.gfan'
    CHANNEL_ID = 'gfan'

    ICON_PATH = '../../../pokemon_icons/android/gfan'

    APPKEY = '1677378043'

    @classmethod
    def rules(cls):
        #NATIVE_MAIN_BOOT = False
        return super(RuleGfan, cls).rules()


@register
class RuleWanka(RuleBase):
    LABEL = 'wanka'
    DIRECTORY = 'wanka'
    CH_NAME = '硬核小包'
    SDKTYPE = '23'
    PACKAGE_NAME = 'com.winnergame.pokemon.wanka'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.wanka'
    CREATE_ORDER_URL = 'http://sdk.fengshen.winnergame.com/sdk/android/sdk/wanka/create_order'
    CHANNEL_ID = 'wanka'


@register
class RuleDownjoy(RuleBase):
    LABEL = 'downjoy'
    DIRECTORY = 'downjoy'
    CH_NAME = '当乐小包'
    SDKTYPE = '38'
    PACKAGE_NAME = 'com.winnergame.pokemon.downjoy'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.downjoy'
    CHANNEL_ID = 'downjoy'

    MERCHANT_ID = '1368'
    APPID = '3749'
    APPKEY = 'dNQsiZIW'

    @classmethod
    def rules(cls):
        return super(RuleDownjoy, cls).rules() + [
            ('src/org/weilan/SplashActivity.java', 'replace', cls.common_replaces()),
        ]


@register
class RuleMZW(RuleBase):
    LABEL = 'mzw'
    DIRECTORY = 'mzw'
    CH_NAME = '拇指玩小包'
    SDKTYPE = '41'
    PACKAGE_NAME = 'com.winnergame.pokemon.mzw'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.mzw'
    CHANNEL_ID = 'muzhiwan'

    APPKEY = 'f3244edd2c89a457b9708eb4e503b37d'

    @classmethod
    def rules(cls):
        return super(RuleMZW, cls).rules() + [
            ('src/org/weilan/SplashActivity.java', 'replace', cls.common_replaces()),
        ]


@register
class RulePPS(RuleBase):
    LABEL = 'pps'
    DIRECTORY = 'pps'
    CH_NAME = 'PPS小包'
    SDKTYPE = '39'
    PACKAGE_NAME = 'com.winnergame.pokemon.pps'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.pps'
    CHANNEL_ID = 'pps'

    GAMEID = '3639'


@register
class RulePPTV(RuleBase):
    LABEL = 'pptv'
    DIRECTORY = 'pptv'
    CH_NAME = 'PPTV小包'
    SDKTYPE = '40'
    PACKAGE_NAME = 'com.winnergame.pokemon.pptv'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.pptv'
    ICON_PATH = '../../../pokemon_icons/android/pptv'
    CHANNEL_ID = 'pptv'

    APPID = 'sqxjl_m'
    PPTV_CID = '269'
    PPTV_CCID = ''
    UMENG_CHANNEL = '269'


@register
class RulePipaw(RuleBase):
    LABEL = 'pipaw'
    DIRECTORY = 'pipaw'
    CH_NAME = '琵琶网小包'
    SDKTYPE = '32'
    PACKAGE_NAME = 'com.winnergame.pokemon.ppw'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.pipaw'
    CHANNEL_ID = 'pipawang'

    APPID = '12381435890541'
    MERCHANT_ID = "1238"
    MERCHANT_APPID = "1301"
    PRIVATE_KEY = "f57d74d191b5fe31143ff28254d47941"

    @classmethod
    def rules(cls):
        return super(RulePipaw, cls).rules() + [
            ('src/org/weilan/SplashActivity.java', 'replace', cls.common_replaces()),
        ]


@register
class RuleEGame(RuleBase):
    LABEL = 'egame'
    DIRECTORY = 'egame'
    CH_NAME = '电信爱游戏小包'
    SDKTYPE = '37'
    PACKAGE_NAME = 'com.winnergame.pokemon.egame'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.egame'
    CHANNEL_ID = 'egame'

    APPID = '5053651'
    APPKEY = 'ac1dd0b898e076b2ed49624c16253924'
    CLIENTID = '16578107'
    CLIENTSECRET = '562b4a48f9584bc69c4a3291dfda1d93'

    EGAME_CHANNEL = '10000000'

    @classmethod
    def rules(cls):
        return super(RuleEGame, cls).rules() + [
            ('extra_assets/feeInfo.dat', 'copy', 'feeInfo_pokemon.dat'),
        ]


@register
class RuleVivo(RuleBase):
    LABEL = 'vivo'
    DIRECTORY = 'vivo'
    CH_NAME = 'VIVO小包'
    SDKTYPE = '42'
    PACKAGE_NAME = 'com.winnergame.pokemon.vivo'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.vivo'
    CHANNEL_ID = 'vivo'

    APPID = "829b98597d987dd831b7f36d92d8fd04"
    CREATE_ORDER_URL = 'http://pokemonpro.sdk.dnastdio.com:8888/sdk/android/sdk/vivo/create_order'

    @classmethod
    def rules(cls):
        return super(RuleVivo, cls).rules() + [
            ('src/org/weilan/wxapi/WXPayEntryActivity.java', 'replace', cls.common_replaces()),
        ]



@register
class RulePaojiao(RuleBase):
    LABEL = 'paojiao'
    DIRECTORY = 'paojiao'
    CH_NAME = '泡椒小包'
    SDKTYPE = '31'
    PACKAGE_NAME = 'com.winnergame.pokemon.paojiao'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.paojiao'
    CHANNEL_ID = 'paojiao'

    APPID = '1274'
    APPKEY = 'LJICymT8uw5gvZBOTw2IPN6V4Ii8QXUe'
    JPUSH_APPKEY = '8172ea4cb6d808cb9fd7ea59'


@register
class RuleZC(RuleBase):
    LABEL = 'zc'
    DIRECTORY = 'zc'
    CH_NAME = '筑巢小包'
    SDKTYPE = '9'
    PACKAGE_NAME = 'com.winnergame.pokemon.zc'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.zc'
    CHANNEL = ''
    CHANNEL_ID = 'zc'

    TD_APPID = '33e15d27544f42d9b5f4f953a44e92e2'
    TD_CHANNEL = ''

    ZC_APPID = '619086295154565120'
    ZC_RSA = 'MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAKSsxVpGBR+BEY0UHNAVoRxN3skQbatVvG3QbO4lm5GLLe1XOzHtHWraMtFiPa4GxhTn1GZFp0dPcvP1EoCbRIyZMkUNmix9rye88kDagpOZSUxUGirnQnT8vxzKhKsMj2JKp6SLIM7BzV2z+iQ7Z2xx/9779OVrj6e9xkhtVCqZAgMBAAECgYBmN3gpGN2FOLCUSa+42jQvRYbMd44blBRqdb2n9WAjb6kKceMkknJ4KQjyP3DZ3QqHX3/QG9xBv2czVyQtADQDswl4urPPQCdPh7P8H2foIxYAIyYnMwK0J8YuHzcs2gVrxQke0jneY+DIZsqcAnVpvzF5ONkxI5zXW40tC+hyoQJBAM/lJAyjzoUT3bw9fW+G90I54N7YUjZCybXIdLc2zD+OQjB5APaGFxmXjR7/qz0sa0WzuAKmG6hE6khSD+5C5AMCQQDKx3EGUhTyeUInwEShR2GrmYs3zDpNJ38cGx5zbZykHFM8iVW6NQSyovv7NVuPaf/irI8FRkR4vrbcetzDMuozAkEAuUInYsAiTAKNCK7+9YCfHDv5gHvinwnbOAu+vnmtf0FlCE78JbMOKLcdga8xyFyp5z4kzu95G/T1labTHW4sQwJAaxcnPrJMs72MTZgB5rbfAxQk7QPjamnIfFxqGYWy6wy2fMr+xkdHwtvGfeWxBC1z4Q9GvP9eG/KEei48tq4F9wJAQen9rksNxrP27XrS3RzW8HUEyZwWXQ2RQ5ToorVyM3bmBl+HwYNdXmKzz3WSOXiAq7cCI9TKPjFOWE83qfx3Vg=='
    PAY_URL = 'http://sdk.fengshen.winnergame.com/sdk/android/zcgame/pay_callback'


ZC_CHANNELS = [
    ('qixiazi', '七匣子'),
    ('youyi', '优艺市场'),
    #('anjingling', '安精灵'),
    ('jufeng', '聚丰网络'),
    ('kaopu', '靠谱助手'),
    ('shouyou', '手游之家'),
    ('anfeng', '安锋网'),
    ('hulizhushou', '狐狸助手'),
    ('fengyou', '疯游网'),
    #('zhidian', '指点传媒'),
    #('wx', 'WX'),
    ('shenma', '神马'),
    ('sougou', '搜狗'),
    ('dashi1', '大使1'),
    ('dashi2', '大使2'),
    ('dashi3', '大使3'),
    ('dashi4', '大使4'),
    ('dashi5', '大使5'),
    ('dashi6', '大使6'),
    ('dashi7', '大使7'),
    ('dashi8', '大使8'),
    ('dashi9', '大使9'),
    ('dashi10', '大使10'),
    ('leiting', '雷霆生动'),
    ('yyh', '应用汇'),
    ('youle', '游乐堂'),
    ('ziliang', '子凉游戏'),
    ('simi', '思蜜创想'),
    ('youxiqun', '游戏群'),
    ('tianxia', '天下江湖'),
    ('qianchi', '千尺'),
    ('sikai', '斯凯'),
    ('tianyu', '天语手机'),
]
for label, name in ZC_CHANNELS:
    register(type('RuleZC%s' % label, (RuleZC,), dict(
        LABEL='zc_%s' % label,
        CH_NAME='筑巢%s小包' % name,
        CHANNEL=label,
        CHANNEL_ID = label,
    )))


@register
class RuleHaima(RuleBase):
    LABEL = 'haima'
    DIRECTORY = 'haima'
    CH_NAME = '海马小包'
    SDKTYPE = '44'
    PACKAGE_NAME = 'com.winnergame.pokemon.ad.hm'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.hm'
    CHANNEL_ID = 'hm'

    ICON_PATH = '../../../pokemon_icons/android/haima'

    APPID = '07958c0f992df0d72e71dfdeaf06d72f'
    APPKEY = '57093e2be9da90b6f7c158a239aa9ad8'
    HM_GAME_CHANNEL = ''

    @classmethod
    def rules(cls):
        return super(RuleHaima, cls).rules() + [
            ('src/org/weilan/SplashActivity.java', 'replace', cls.common_replaces()),
        ]


@register
class RuleXY(RuleBase):
    LABEL = 'xyandroid'
    DIRECTORY = 'xyandroid'
    CH_NAME = 'XY小包'
    SDKTYPE = '45'
    PACKAGE_NAME = 'com.winnergame.pokemon.xyandroid'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.xyandroid'
    CHANNEL_ID = 'xy'

    APPID = '10000304'
    APPKEY = 'OJjkDM9ZAjYNDzdDgQCKaXDWilt0nJnM'


@register
class RuleWO17(RuleBase):
    LABEL = 'wo17'
    DIRECTORY = 'wo17'
    CH_NAME = '17WO小包'
    SDKTYPE = '46'
    PACKAGE_NAME = 'com.winnergame.pokemon.wo17'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.wo17'
    CHANNEL_ID = 'wo17'

    APPID = '400556'
    APPKEY = '88cf91a1aef212f3c2cd12406983427d'
    APPSECRET = 'MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAIfdmhoEHp23e31Psvj9Bv+XlxnqpLqOfszO0XwcIt5ZUoSkvb7nbg4LT1gDeJka4U9DJ1l7m5VXfuXjp97qkKsCAwEAAQ=='

@register
class RuleMoLi(RuleBase):
    LABEL = 'moli'
    DIRECTORY = 'moli'
    CH_NAME = '墨狸小包'
    SDKTYPE = '47'
    PACKAGE_NAME = 'com.winnergame.pokemon.moli'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.moli'
    CHANNEL_ID = 'moli'

    APPID = '3002650777'
    CPPKEY = 'MIICXgIBAAKBgQDSQEvPkbjVJ5JPpcY6DJrq2A07QdFkXnkjBXEzgmO669uGRwNkK8XUqFfzpwn49V0gEUINbmiWjyECBoK9zg0dVm6OUyNCIE5MtGx7V9cEpTsFMoPidIn/4sbsQqv/Eef9lGCSToxIlbpQNO0xpm8eBCz+6ZyQIuLgsRNeLhN5EwIDAQABAoGBALdpdXjuw1HXQnCOyd0L7/zcWraN1S98pqohbj4kCgIfDJMX0eKJuPupm4gm+LEgwotd4sQ6w6xL0dyld1pCrPaLM3gjA04qxGKgMpsGPtMfCuwu0lb/x3JVIljqigBXFtRIppN+s0mJFPYv4TCOqpebFo92f5KLs/OCL0xIfathAkEA/1giJxfN6oIuDy10AEIo938N2fEmCXll1Czo7e5h/k3dccXj7+HL9/yoG3ekNmVkosVYikeHwI0OwK1cDdO6kQJBANLKhJd/FCk/gr51qm20+cdrLmkbes335//ZRUWDFt9HPEM1KhXl9tqVOJAR3s8MEuJTBvVJ8zPykZ1r29Loo2MCQQC4mer3AEqqQ7sw1deLaEldxMkqyyCIsO9hWaZ8fV7zDzANVNfZURC5FDwkv3ZErUD4PFwqfFQ0bMZBnhNzG6NBAkA/oSBrNtIYLXLDGXPL0BCCMQl+cuwcFpRyt9xgQlT6K1+2jerZV2Sv0NGVM7/FUki1BwkXrC385WEtWuytesovAkEA6QxUmkrLpItVHNrdg9FPBbydUlXsYO5AN0XdF6vzo4Y6Mz5+lTRO64M40gn6OpNodmI+4fU3M3G/ju0lgIWJtw=='
    PUBLICKEY = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC0eAOhgqPXHn8d0iOuOt/RkjxzIE7Fjo7KkaiUEMLDLUaVe29vKMFPx6Di4fCbqOZZia02ZhgXikKrrZKcVBoJ/6hn7obwPcN2NBa12uacNqbtPILaNM7Zyd567EZXE7pNNwZDaiCRYDPLV5UXcT8aw4HixhiH2L09RUtw4JTxiwIDAQAB'

@register
class RuleHuawei(RuleBase):
    LABEL = 'huawei'
    DIRECTORY = 'huawei'
    CH_NAME = '华为小包'
    SDKTYPE = '48'
    PACKAGE_NAME = 'com.winnergame.pokemonpro.huawei'
    YY_PACKAGE_NAME = 'com.winnergame.pokemonpro.huawei'
    CHANNEL_ID = 'huawei'

    APPID = '10430315'
    PAYID = '900086000022190346'
    PUBLIC_KEY = 'MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKQM73iEYW/f6JtRgOuwsyvvk1hfKNUnC3F0arwr8+YqrIOrPZMA+5fzV6hMH4Pqeinp7QtRrWwKycH96dWPt08CAwEAAQ=='
    GET_BUOY_PRIVATE_KEY = 'http://pokemonpro.sdk.dnastdio.com:8888/sdk/android/sdk/huawei/buoy'
    GET_PAY_PRIVATE_KEY = 'http://pokemonpro.sdk.dnastdio.com:8888/sdk/android/sdk/huawei/pay'

    @classmethod
    def rules(cls):
        return super(RuleHuawei, cls).rules() + [
            ('src/org/weilan/GlobalParam.java', 'replace', cls.common_replaces()),
        ]

@register
class RuleWeilan(RuleBase):
    LABEL = 'weilan'
    DIRECTORY = 'weilan'
    CH_NAME = '微蓝小包'
    SDKTYPE = '49'
    PACKAGE_NAME = 'com.winnergame.pokemon.weilan'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.weilan'
    CHANNEL_ID = 'weilan'
    CHANNEL = ''

    APP_KEY    = '5i29qfd23a4bghaswx9w'
    APP_SECRET = 'psyvmyra6f7of4sacvpu'
    SERVER_ID  = 'M1028A'
    #PROJECT_ID = 'P10116A'
    PRODUCT_ID = 'D10053A'

    @classmethod
    def rules(cls):
        return super(RuleWeilan, cls).rules() + [
            ('src/org/weilan/WLSdkConfig.java', 'replace', cls.common_replaces()),
        ]

#       label           name             project_id
WL_CHANNELS = [
    ( '1',         '1',    'P10124A', ),
    ( '2',         '2',    'P10125A', ),
    ( '3',         '3',    'P10126A', ),
    ( '4',         '4',    'P10127A', ),
    ( '5',         '5',    'P10128A', ),
    ( '6',         '6',    'P10129A', ),
    ( '7',         '7',    'P10130A', ),
    ( '8',         '8',    'P10131A', ),
    ( '9',         '9',    'P10132A', ),
    ( '10',        '10',   'P10133A', ),
    ( '11',        '11',   'P10134A', ),
    ( '12',        '12',   'P10135A', ),
    ( '13',        '13',   'P10136A', ),
    ( '14',        '14',   'P10137A', ),
    ( '15',        '15',   'P10138A', ),
    ( '16',        '16',   'P10139A', ),
    ( '17',        '17',   'P10140A', ),
    ( '18',        '18',   'P10141A', ),
    ( '19',        '19',   'P10142A', ),
    #( '20',        '20',   'P10143A', ),
]
for label, name, project_id in WL_CHANNELS:
    register(type('RuleWeilan%s' % label, (RuleWeilan,), dict(
        LABEL='weilan_%s' % label,
        CH_NAME='微蓝CPS_%s小包' % name,
        PROJECT_ID = project_id,
        CHANNEL_ID = label,
        CHANNEL = label,
    )))

@register
class RuleWeilanYyb(RuleBase):
    LABEL = 'weilanyyb'
    DIRECTORY = 'weilan'
    CH_NAME = '微蓝_应用宝_小包'
    SDKTYPE = '49'
    PACKAGE_NAME = 'com.tencent.tmgp.klsqxjl'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.weilan'
    CHANNEL_ID = 'weilan_yyb'
    CHANNEL = 'weilan_yyb'

    APP_KEY    = '5i29qfd23a4bghaswx9w'
    APP_SECRET = 'psyvmyra6f7of4sacvpu'
    SERVER_ID  = 'M1028A'
    PROJECT_ID = 'P10143A'
    PRODUCT_ID = 'D10053A'

    @classmethod
    def rules(cls):
        return super(RuleWeilanYyb, cls).rules() + [
            ('src/org/weilan/WLSdkConfig.java', 'replace', cls.common_replaces()),
        ]

@register
class RuleLenovo(RuleBase):
    LABEL = 'lenovo'
    DIRECTORY = 'lenovo'
    CH_NAME = '联想小包'
    SDKTYPE = '50'
    PACKAGE_NAME = 'com.winnergame.pokemon.lenovo'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.lenovo'
    CHANNEL_ID = 'lenovo'

    ICON_PATH = '../../../pokemon_icons/lianxiang'

    OPEN_APPID = '1511180153656.app.ln'
    PAY_APPKEY = 'MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAJ3oZzcR7MWIkpyUOv133CgRLbs7IrcHj4VHOHgZl7+naUDpqAXf8BfxzoQJDRJy7zsRADvu044w5UU9Pntbb+eRWQipdArfZ30RRsCA2lwXwbzMuzaGBmlrqwyeZOHS9uU3vQ6oPoIp+ZYpBaEJN8Io3MoxGMy0/0i7V1BMjbTRAgMBAAECgYAky22ZmHSqhqtbDvM78rz7HR2h3iK1sW5Q6QqQea4xe2n8NTXwwICqo66yd4VzQhLamZiLXpgvLteNrbqsdd76IOyAgnHbXHhNLR9HZWAG5iRxjChOAI3B1Hw+6CgFbKA2Z5MAGu1VYzpYdXI364GME1XzoVVuxUsWTK+Qrjw87QJBAOf00NJhvMJmT1RSnaGHmdZjfNBU73U+uv2Z5VxCNUs+rkhgtBt9Rodll3Ut0z41Gri/wORKgweUsBcRX7bnLNsCQQCuRqO3UJGzECNNzVG/7zGqK3GuNzPBiqNPvXHzexwqjW7P9JMLiDbH6mJRBpoukBBQcja5oqZeemC4sZuHRL7DAkAgpYxej/MJSW0Q6S/WdEdqrUX77HhngBTBbM+jVI47sO5GsRWoaNFsbRgMHg8FSmQgbJyxhOs8Pekq1f8qtw7RAkBXV2XDgKiUsljPLEB1Td55J27A3j+dFutEEnDikueJ1/oaVLvBQtIZnTkK3KE3BtJ2Ttdob8Crhu+kgLaus2BbAkEApwxWPb3UEFaQBIwdHALNjF/sQzflbJavCyOLBL3D53hvQ1rOPV9f0FFvozaPy8fnKOC4PPQXGkGNsrC+R+F6Bw=='

    @classmethod
    def rules(cls):
        cls.BASE_ACTIVITY = """
                <activity android:name="org.weilan.poem"
                          android:label="@string/app_name"
                          android:screenOrientation="portrait"
                          android:theme="@android:style/Theme.NoTitleBar.Fullscreen"
                          android:configChanges="keyboardHidden|orientation">
                    <intent-filter>
                        <action android:name="lenovoid.MAIN" />
                        <category android:name="android.intent.category.DEFAULT" />
                    </intent-filter>
                </activity>

                <activity android:name="org.weilan.VideoActivity"
                    android:label="@string/app_name"
                    android:screenOrientation="portrait"
                    android:configChanges="keyboardHidden|orientation|screenSize|layoutDirection">
                    >
                    <intent-filter>
                        <action android:name="org.weilan.VideoActivity" />
                        <category android:name="android.intent.category.DEFAULT"/>
                    </intent-filter>
                </activity>

                <receiver android:name="org.weilan.PushReceiver" >
                    <intent-filter android:priority="2147483647" >
                        <action android:name="android.intent.action.BOOT_COMPLETED"/>
                        <category android:name="android.intent.category.DEFAULT" />
                        <action android:name="android.intent.action.USER_PRESENT"/>
                    </intent-filter>
                </receiver>

                <service
                    android:name="org.weilan.PushService"
                    android:enabled="true"
                    />
        """
        return super(RuleLenovo, cls).rules() + [
            ('src/org/weilan/SdkConfig.java', 'replace', cls.common_replaces()),
        ]

@register
class RuleAmigo(RuleBase):
    LABEL = 'amigo'
    DIRECTORY = 'amigo'
    CH_NAME = '金立小包'
    SDKTYPE = '51'
    PACKAGE_NAME = 'com.winnergame.pokemon.am'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.am'
    CHANNEL_ID = 'amigo'

    ICON_PATH = '../../../pokemon_icons/jinli'

    APP_KEY    = '11B5BA6537274E798CEED85864AC63CF'
    ORDER_URL  = 'http://pokemonpro.sdk.dnastdio.com:8888/sdk/android/sdk/gionee/create_order'

    @classmethod
    def rules(cls):
        return super(RuleAmigo, cls).rules() + [
            ('src/org/weilan/SdkConfig.java', 'replace', cls.common_replaces()),
        ]

@register
class RuleYouku(RuleBase):
    LABEL = 'youku'
    DIRECTORY = 'youku'
    CH_NAME = '优酷小包'
    SDKTYPE = '33'
    PACKAGE_NAME = 'com.winnergame.pokemon.youku'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.youku'
    CHANNEL_ID = 'youku'

    APPID      = '2512'
    APPKEY     = 'f8096fefaa88dbad'
    APPSECRET  = '6512508a115233327d2c91ceb78ed77f'
    YOUKU_VERSION_CODE = ''

    PAY_URL = 'http://pokemonpro.sdk.dnastdio.com:8888/sdk/android/sdk/youku/pay_callback'

    @classmethod
    def rules(cls):
        codeNum = int(RuleBase.VERSION_CODE)
        cls.YOUKU_VERSION_CODE = str(codeNum/10000) + str(codeNum%100)
        print 'YOUKU_VERSION_CODE = ' + cls.YOUKU_VERSION_CODE
        return super(RuleYouku, cls).rules() + [
            ('src/org/weilan/GameProxyImpl.java', 'replace', cls.common_replaces()),
        ]

@register
class RuleGuopan(RuleBase):
    LABEL = 'guopan'
    DIRECTORY = 'guopan'
    CH_NAME = 'XX果盘小包'
    SDKTYPE = '55'
    PACKAGE_NAME = 'com.winnergame.pokemon.ad.guopan'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.guopan'
    CHANNEL_ID = 'guopan'
    ICON_PATH = '../../../pokemon_icons/android/xx'

    APPID      = '102121'
    APPKEY     = 'CJOVUCOA7728E002'

@register
class RuleM4399(RuleBase):
    LABEL = 'm4399'
    DIRECTORY = 'm4399'
    CH_NAME = 'm4399小包'
    SDKTYPE = '30'
    PACKAGE_NAME = 'com.winnergame.pokemonpro.m4399'
    YY_PACKAGE_NAME = 'com.winnergame.pokemonpro.m4399'
    ICON_PATH = '../../../pokemon_icons/android/4399'
    CHANNEL_ID = 'm4399'

    APPKEY     = '110522'

@register
class RuleMz(RuleBase):
    LABEL = 'mz'
    DIRECTORY = 'mz'
    CH_NAME = '魅族小包'
    SDKTYPE = '57'
    PACKAGE_NAME = 'com.winnergame.pokemon.mz'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.mz'
    CHANNEL_ID = 'meizu'

    APPID     = '2820741'
    APPKEY    = 'e158c5bd9d2c49a29c890e5a588d9952'
    ORDER_URL = 'http://pokemonpro.sdk.dnastdio.com:8888/sdk/android/sdk/meizu/create_order'

@register
class RuleKaopu(RuleBase):
    LABEL = 'kaopu'
    DIRECTORY = 'kaopu'
    CH_NAME = '靠谱小包'
    SDKTYPE = '56'
    PACKAGE_NAME = 'com.winnergame.pokemon.kaopu'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.kaopu'
    CHANNEL_ID = 'kaopu'

    APPID      = '10216001'
    APPKEY     = '10216'
    APPSECRET  = 'B7FA47A6-3765-4DE8-8DC5-7C8355D7C7C5'
    SDKVERSION = '1.0'

    @classmethod
    def rules(cls):
        cls.VERSION_NAME = "1.0"
        return super(RuleKaopu, cls).rules()

@register
class RuleCpad(RuleBase):
    LABEL = 'cpad'
    DIRECTORY = 'cpad'
    CH_NAME = '酷派小包'
    SDKTYPE = '52'
    PACKAGE_NAME = 'com.winnergame.pokemon.cpad'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.cpad'
    CHANNEL_ID = 'cpad'

    APPID      = '5000002454'
    APPKEY     = '4bcd7fccf85b4adeb438a3e9f97e9f82'
    PRIVATEKEY = 'MIICXAIBAAKBgQCMsXOwu4D6Osxv/CRuafTTBZBhqCiDewMjqb71EMQsj290Wu3rXFlWhtxfQ6d/st5CBlgkIc0TYYrJSer2u8DQcQvZNqqGeRrVuQlSmIy31KeKK5wZH5TWAGXz7Des4oqo1jZIAlXbrIC2d2k+WLIB+0PGv8KCvyBGW5r9zxOa7QIDAQABAoGAHo4XWwWNwEpuxc9TtisKwZ2OurbDfbKEfwVJdH2crTTFdtacnyXiPRly2LmfsesNu/cWw1oX6KKheo+0GLuz5vuAYTNnk1VobOWqPdDzdmsxca9pdZMOLLu2ueToY66obipfWwzitiC6Fv4pUp6m1W1clZ3aDIEfG42gWgpD4wECQQD4peydEJK4WRS3ph76JlipEve9Jm9U/hZYKMS0jWpsMwMxKV3ZN8RF9ftQGPpp+sJwliwmeswnSCFhYV72vTRBAkEAkNpkLWGkPEqkiAfuHa81vF+Dr2x9jbo9VHfc77bpUit1LM1ceka9iGNq+9pQjzM1d0CtyEjXCZjbM79If9iLrQJBAJMrcj8MvirK3w5MDu20oKmCBow4IZFGyubnSnYrdaARGYSRnXCiJ1PZYiRohF8SAuAsonksGYXulYNT5KdaGYECQCEn7BA7LlWinECK2CUxSrKAhmrsAV0kiQ9BlG/GRWfKjLqhkw5mDNIgN4fIc/IjPZS7WEvk6FvJAju5CAZDcc0CQFU7EeMriSO6ArT6XNSIfq9GhVm+BLQ08YVzhPCmUGyC339BUb+nRMmfnUnJsqYMhsJplaZdyLCAF6Zbhequ0Ug='
    PAY_URL    = 'http://pokemonpro.sdk.dnastdio.com:8888/sdk/coolpad/pay_callback'
    #PAY_URL    = ''

@register
class RuleBaidu2(RuleBase):
    APPNAME = '萌宠小精灵'
    LABEL = 'baidu2'
    DIRECTORY = 'baidu'
    CH_NAME = '萌宠百度小包'
    SDKTYPE = '58'
    PACKAGE_NAME = 'com.winnergame.sprite.baidu'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.baidu'
    CHANNEL_ID = 'baidu'

    ICON_PATH = '../../../pokemon_icons/baidu/baidu2'

    APPID = '7398765'
    APPKEY = 'mMdG57EWUYFMEb19cQSVoCFx'

@register
class RuleWeilan2(RuleBase):
    APPNAME = '萌宠小精灵'
    LABEL = 'weilan2'
    DIRECTORY = 'weilan'
    CH_NAME = '萌宠微蓝小包'
    SDKTYPE = '59'
    PACKAGE_NAME = 'com.winnergame.sprite.weilan'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.weilan'
    CHANNEL_ID = 'weilan'

    APP_KEY    = 'attgos3er5dk2ekrifa7'
    APP_SECRET = 'rv29y983xdmkzywi3op8'
    SERVER_ID  = 'M1029A'
    PROJECT_ID = 'P10117A'
    PRODUCT_ID = 'D10054A'

    @classmethod
    def rules(cls):
        return super(RuleWeilan2, cls).rules() + [
            ('src/org/weilan/WLSdkConfig.java', 'replace', cls.common_replaces()),
        ]

@register
class RuleHaoMeng(RuleBase):
    LABEL = 'haomeng'
    DIRECTORY = 'haomeng'
    CH_NAME = '好盟小包'
    SDKTYPE = '60'
    PACKAGE_NAME = 'com.winnergame.pokemon.haomeng'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.haomeng'
    CHANNEL_ID = 'haomeng'

    APP_ID     = '516'
    APP_KEY    = 'yWpx3hWQHFhSnTCj#516#6KuRKuaAjLJ5sYRy'

    @classmethod
    def rules(cls):
        return super(RuleHaoMeng, cls).rules() + [
            ('src/org/weilan/GameProxyImpl.java', 'replace', cls.common_replaces()),
        ]

@register
class RuleCCPlay(RuleBase):
    LABEL = 'ccplay'
    DIRECTORY = 'ccplay'
    CH_NAME = '虫虫小包'
    SDKTYPE = '61'
    PACKAGE_NAME = 'com.winnergame.pokemon.ccplay'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.ccplay'
    ICON_PATH = '../../../pokemon_icons/android/congcong'
    CHANNEL_ID = 'ccplay'

    APP_ID     = '103733'
    APP_KEY    = '6ca9f06072da43b98f013a7829a15d4d'

    @classmethod
    def rules(cls):
        return super(RuleCCPlay, cls).rules() + [
            ('src/org/weilan/GameProxyImpl.java', 'replace', cls.common_replaces()),
        ]

@register
class RuleYYB(RuleBase):
    LABEL = 'yyb'
    DIRECTORY = 'yyb'
    APPNAME = '神奇小精灵'
    CH_NAME = '应用宝小包'
    SDKTYPE = '24'
    PACKAGE_NAME = 'com.tencent.tmgp.com.winnergame.pokemon.weilan'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.yyb'
    ICON_PATH = '../../../pokemon_icons/android/yunliang'
    CHANNEL_ID = 'yyb'

    QQ_APPID = '1104928607'
    #QQ_APPKEY = 'moGFruUJK4I6Re5C'
    QQ_APPKEY = 'ihNyP0xCjLGuLx0kog3SnU72H4Ccjtx1'
    WX_APPID = 'wx84325ed5efe57c0d'
    MSDK_KEY = '73d3493fa8ffea3701e47e6c9657549c'


    #CREATE_ORDER_URL  = 'http://pokemonpro.sdk.dnastdio.com:8888/sdk/android/sdk/yyb/create_order'
    ZONE_INFO_URL     = 'http://pokemonpro.sdk.dnastdio.com:8888/sdk/android/sdk/yyb/info'
    QUERY_BALANCE_URL = 'http://pokemonpro.sdk.dnastdio.com:8888/sdk/android/sdk/yyb/query_balance'
    #ZONE_INFO_URL     = 'http://pokemonpro.sdktest.dnastdio.com:8888/sdk/android/sdk/yyb/info'
    #QUERY_BALANCE_URL = 'http://pokemonpro.sdktest.dnastdio.com:8888/sdk/android/sdk/yyb/query_balance'

    @classmethod
    def rules(cls):
        return super(RuleYYB, cls).rules() + [
            ('src/com/tencent/tmgp/com/winnergame/pokemon/weilan/wxapi/WXEntryActivity.java', 'replace', cls.common_replaces()),
        ]

@register
class RuleYiJie(RuleBase):
    LABEL = 'yijie'
    DIRECTORY = 'yijie'
    CH_NAME = '易接母包'
    SDKTYPE = '62'
    PACKAGE_NAME = 'com.winnergame.pokemonpro.yj'
    YY_PACKAGE_NAME = 'com.winnergame.pokemonpro.yijie'
    CHANNEL_ID = 'yijie'

    APP_ID     = '{D848E772-DB4FAEFE}'
    PAY_URL = 'http://pokemonpro.sdk.dnastdio.com:8888/sdk/yijie/pay_callback'

    @classmethod
    def rules(cls):
        return super(RuleYiJie, cls).rules() + [
            ('src/org/weilan/GameProxyImpl.java', 'replace', cls.common_replaces()),
        ]

@register
class RuleHTC(RuleBase):
    LABEL = 'htc'
    DIRECTORY = 'htc'
    CH_NAME = 'HTC小包'
    SDKTYPE = '64'
    PACKAGE_NAME = 'com.winnergame.pokemonpro.htc'
    YY_PACKAGE_NAME = 'com.winnergame.pokemonpro.htc'
    CHANNEL_ID = 'htc'

    CP_GAME_CODE = '2904148438271'
    PAY_URL = 'http://pokemonpro.sdk.dnastdio.com:8888/sdk/htc/pay_callback'
    CP_PRIVATE_KEY_PKCS8 = "MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAKMGKvMyo8LkwiDobtp5KDR4KcdK39CBMPdYYUrmfX9WLKjCQJmmjmi9WlTn/YywD2gyISEDNuG1Qpw09nqeECoueCo7mpXZMhqPPCF6DsODeW3Q1vKYasrfH+RSYJJVWVJIhc+JdupRf9d8rdl1Sfs4PQpWhkjyU5rEyF+yQgIlAgMBAAECgYAvQLZqT59P+maai0S2Zq/UpY/WiElfclLzHtb0kuKFakD/mW6IGtLkYR4xxhykDtQoa39Wxku+GH/6Lw/ScsZUPTRqAGY+WDQp0Ss9JlB5FRcotliL0ZbTfgKLSY6Oj5IaWKV9ypzwrklEWI14u0vgokpIFC7Ee5Io+vJa4ldOcQJBANGFdEehXY/Tw+xMUQtKFg3qNVcr3wQ2UZoGvcAOCYiVI2luYRXaumtj9H4QC/LMDz7tQUw3Gz6HkeKG4nfERG8CQQDHMCykrKLhPfewnVxMTOgIuEXS3apFhTXgRDRDKdVs9143xOwa86Hd45LCAGEzuhT3me2b+qUSotfQecveOnSrAkEAzdNZWKjX3dv9o1uRXhLIuaC0B8+MRXoLDdHDhDEGAovn/sG1VB/MdIT8AP9IjZsS+xFdzT5xYCsUEEHLpjZDtwJBALl0FvyzZ2tDYMvllzvLFvaXaxsrGw9jOYg2uFoYJwgvQF+4TwPA9mI7MjbCV73rcP4fKOVi9jJlv33xCGk+D8UCQCf79vgHU7Zm8tXEQWwsWmwHPY9k0I4o6VyOAPxyIBEVsDDyPLoZWs2yVR/KCX0PT3MDwKWh"

    @classmethod
    def rules(cls):
        return super(RuleHTC, cls).rules() + [
            ('src/org/weilan/GameProxyImpl.java', 'replace', cls.common_replaces()),
        ]

@register
class RuleTiantian(RuleBase):
    LABEL = 'tiantian'
    DIRECTORY = 'tiantian'
    CH_NAME = '天天小包'
    SDKTYPE = '63'
    PACKAGE_NAME = 'com.winnergame.pokemonpro.ltbl'
    YY_PACKAGE_NAME = 'com.winnergame.pokemonpro.ltbl'
    CHANNEL_ID = 'tiantian'

    APPID   = 'LT20160107-118'
    PAY_URL = 'http://pokemonpro.sdk.dnastdio.com:8888/sdk/tiantian/pay_callback'

    @classmethod
    def rules(cls):
        return super(RuleTiantian, cls).rules() + [
            ('src/org/weilan/GameProxyImpl.java', 'replace', cls.common_replaces()),
        ]

@register
class RuleMumayi(RuleBase):
    LABEL = 'mumayi'
    DIRECTORY = 'mumayi'
    CH_NAME = '木蚂蚁小包'
    SDKTYPE = '66'
    PACKAGE_NAME = 'com.winnergame.pokemonpro.mumayi'
    YY_PACKAGE_NAME = 'com.winnergame.pokemonpro.mmy'
    CHANNEL_ID = 'mumayi'

    APP_KEY = 'a192bfc26e8139fedUp2QhpSDo7KPdHZUXWQgKmFLNhaypH8PWwqzZdLfTAeYVLzuQZl'

    @classmethod
    def rules(cls):
        return super(RuleMumayi, cls).rules() + [
            ('src/org/weilan/GameProxyImpl.java', 'replace', cls.common_replaces()),
        ]

@register
class RuleH07073(RuleBase):
    LABEL = 'h07073'
    DIRECTORY = 'h07073'
    CH_NAME = '07073小包'
    SDKTYPE = '67'
    PACKAGE_NAME = 'com.winnergame.pokemonpro.shuyou'
    YY_PACKAGE_NAME = 'com.winnergame.pokemonpro.h07073'
    CHANNEL_ID = 'h07073'

    PID = '399'
    APP_ID = '370'

    @classmethod
    def rules(cls):
        return super(RuleH07073, cls).rules() + [
            ('src/org/weilan/GameProxyImpl.java', 'replace', cls.common_replaces()),
        ]

@register
class RulePyw(RuleBase):
    LABEL = 'pyw'
    DIRECTORY = 'pyw'
    CH_NAME = '朋友玩小包'
    SDKTYPE = '68'
    PACKAGE_NAME = 'com.winnergame.pokemonpro.yq'
    YY_PACKAGE_NAME = 'com.winnergame.pokemonpro.pyw'
    CHANNEL_ID = 'pyw'

    APPID = '2db467fa'

@register
class RuleLiulian(RuleBase):
    LABEL = 'liulian'
    DIRECTORY = 'liulian'
    CH_NAME = '榴莲小包'
    SDKTYPE = '69'
    PACKAGE_NAME = 'com.tencent.tmgp.mcxjl.ll'
    YY_PACKAGE_NAME = 'com.winnergame.pokemonpro.ll'
    CHANNEL_ID = 'liulian'

    APPID = '69f0456c269a8dff6cfae986679b55ae'
    APPKEY = 'acab48e810a53c0182e49762d39c9efc'
    PRIVATEKEY = '545908c7a34c01112cbd36cb78dd9e01'


@register
class RuleMoge(RuleBase):
    LABEL = 'moge'
    DIRECTORY = 'moge'
    CH_NAME = '魔格小包'
    SDKTYPE = '70'
    PACKAGE_NAME = 'com.winnergame.pokemonpro.mg'
    YY_PACKAGE_NAME = 'com.winnergame.pokemonpro.mg'
    CHANNEL_ID = 'moge'
    ICON_PATH = '../../../pokemon_icons/android/moge'

    APP_ID = '30'
    GAME_ID = '37'
    AGENT = 'default'

    @classmethod
    def rules(cls):
        return super(RuleMoge, cls).rules() + [
            ('src/org/weilan/GameProxyImpl.java', 'replace', cls.common_replaces()),
        ]

@register
class Rule49you(RuleBase):
    LABEL = 'sjyx'
    DIRECTORY = 'sjyx'
    APPNAME = '宠物精灵OL'
    CH_NAME = '49小包'
    SDKTYPE = '71'
    PACKAGE_NAME = 'com.winnergame.cwjlol.sjyou'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.sjyx'
    CHANNEL_ID = 'sjyx'
    CHANNEL = 'sjyx'
    ICON_PATH = '../../../pokemon_icons/android/49you'

    APP_ID    = '444'
    APP_KEY   = '451f2b3ec53014314fa27227739010d2'
    APP_AGENT = ''

    @classmethod
    def rules(cls):
        return super(Rule49you, cls).rules() + [
            ('src/org/weilan/GameProxyImpl.java', 'replace', cls.common_replaces()),
        ]


@register
class RuleJodo(RuleBase):
    LABEL = 'jodo'
    DIRECTORY = 'jodo'
    APPNAME = '萌寵訓練師'
    CH_NAME = 'jodo小包'
    SDKTYPE = '2'
    PACKAGE_NAME = 'com.cuteb.fairy.xh'
    YY_PACKAGE_NAME = 'com.winnergame.pokemon.jodoA'
    CHANNEL_ID = 'jodoAndroid'
    CHANNEL = 'jodoAndroid'
    ICON_PATH = '../../../pokemon_icons/android/zhuodong'

    CP_ID     = 'szweilan'
    GAME_ID   = 'mengchongxunlianshi'
    PAY_CHANNEL = 'jd001'
    FB_APP_ID = '975164579265554'

    @classmethod
    def rules(cls):
        return super(RuleJodo, cls).rules() + [
            ('src/org/weilan/GameProxyImpl.java', 'replace', cls.common_replaces()),
        ]
