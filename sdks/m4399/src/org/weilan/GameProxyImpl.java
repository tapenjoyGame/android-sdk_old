package org.weilan;

import java.util.UUID;
import org.json.JSONObject;
import org.json.JSONException;

import android.app.Activity;
import android.content.Intent;
import android.content.Context;
import android.util.Log;
import android.os.Handler;
import android.os.Bundle;
import android.os.Message;
import android.widget.Toast;
import android.content.pm.ActivityInfo;

import cn.m4399.operate.OperateCenter;
import cn.m4399.operate.OperateCenter.OnCheckFinishedListener;
import cn.m4399.operate.OperateCenter.OnDownloadListener;
import cn.m4399.operate.OperateCenter.OnLoginFinishedListener;
import cn.m4399.operate.OperateCenter.OnQuitGameListener;
import cn.m4399.operate.OperateCenter.OnRechargeFinishedListener;
import cn.m4399.operate.OperateCenterConfig;
import cn.m4399.operate.OperateCenterConfig.PopLogoStyle;
import cn.m4399.operate.OperateCenterConfig.PopWinPosition;
import cn.m4399.operate.UpgradeInfo;
import cn.m4399.operate.User;

public class GameProxyImpl extends GameProxy{
    private OperateCenter mOpeCenter;

    public boolean supportLogin() {
        return true;
    }

    public boolean supportCommunity() {
        return false;
    }

    public boolean supportPay() {
        return true;
    }

    private void initSDK(Activity activity) {
        // 游戏接入SDK；
        mOpeCenter = OperateCenter.getInstance();

        // 配置sdk属性,比如可扩展横竖屏配置
        OperateCenterConfig opeConfig = new OperateCenterConfig.Builder(activity)
            .setDebugEnabled(false)
            .setOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT)
            .setPopLogoStyle(PopLogoStyle.POPLOGOSTYLE_ONE)
            .setPopWinPosition(PopWinPosition.POS_LEFT)
            .setSupportExcess(false)
            .setGameKey("${APPKEY}")
            .build();
        mOpeCenter.setConfig(opeConfig);

        //初始化SDK，在这个过程中会读取各种配置和检查当前帐号是否在登录中
        //只有在init之后， isLogin()返回的状态才可靠
        mOpeCenter.init(activity, new OperateCenter.OnInitGloabListener() {

            // 初始化结束执行后回调
            @Override
            public void onInitFinished(boolean isLogin, User userInfo) {
                //String loginState = isLogin ? getString(R.string.logging) : getString(R.string.not_logging);
                assert(isLogin == mOpeCenter.isLogin());
                //showInToast(loginState + ": " + userInfo);
            }

        // 注销帐号的回调， 包括个人中心里的注销和logout()注销方式
        @Override
        public void onUserAccountLogout(boolean fromUserCenter, int resultCode) {
            userListerner.onLogout(null);
        }

        // 个人中心里切换帐号的回调
        @Override
        public void onSwitchUserAccountFinished(User userInfo) {
            userListerner.onLogout(null);
            org.weilan.User u = new org.weilan.User();
            u.userID = userInfo.getUid();
            u.token = userInfo.getState();
            userListerner.onLoginSuccess(u, null);
        }
        });
    }

    private void destroySDK() {
        if (mOpeCenter != null) {
            mOpeCenter.destroy();
            mOpeCenter = null;
        }
    }

    @Override
    public void onDestroy(Activity activity) {
        super.onDestroy(activity);
        destroySDK();
    }

    public void applicationInit(Activity activity) {
        initSDK(activity);
    }

    public void pay(Activity activity, String ID, String name, String orderID, float price, String callBackInfo, JSONObject roleInfo, final PayCallBack payCallBack) {
        String worldID;
        try {
            worldID = roleInfo.getString("serverID");
        } catch (JSONException e) {
            return;
        }

        Log.v("sdk", "mark:" + worldID + "_" + orderID);
        mOpeCenter.recharge(activity, (int)price, worldID + "_" + orderID, name, new OnRechargeFinishedListener() {
            @Override
            public void onRechargeFinished(boolean success, int resultCode, String msg) {
                if (success) {
                    payCallBack.onSuccess("充值成功");
                }
                else {
                    Log.v("sdk", "pay fail:" + resultCode + "," + OperateCenter.getResultMsg(resultCode));
                    payCallBack.onFail(OperateCenter.getResultMsg(resultCode));
                }
            }
        });
    }

    public void setExtData(Context context, String ext) {
        // 上报角色数据给sdk，ext:json数据，格式如下
        /* local info = {
         *     state = send_type,                   -- type
         *     id = roleId,                      -- roleId
         *     name = roleName,                    -- roleName
         *     level = roleLevel,                   -- roleLevel
         *     serverID = zoneId,                      -- zoneId
         *     serverName = zoneName,                    -- zoneName
         *     gold = balance,                     -- balance
         *     vip = vip,                         -- vip 
         *     factionName = partyName                    -- partyName 
         * }
         */
        // need set server id 
        try {
            JSONObject roleInfo = new JSONObject(ext);
            String serverId     = roleInfo.optString("serverID");
            mOpeCenter.setServer(serverId);
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }

    public void exit(Activity activity, ExitCallback callback) {
        mOpeCenter.shouldQuitGame(activity, new OnQuitGameListener() {
            @Override
            public void onQuitGame(boolean shouldQuit) {
                if (shouldQuit) {
                    destroySDK();
                    poem.quitApplication();
                }
            }
        });
    }

    public void logout(Activity activity, Object customParams) {
        mOpeCenter.logout();
    }

    public void login(Activity activity, Object customParams) {
        mOpeCenter.login(activity, new OnLoginFinishedListener() {
            @Override
            public void onLoginFinished(boolean success, int resultCode, User userInfo) {
                if (success) {
                    org.weilan.User u = new org.weilan.User();
                    u.userID = userInfo.getUid();
                    u.token = userInfo.getState();
                    userListerner.onLoginSuccess(u, null);
                } else {
                    String msg = OperateCenter.getResultMsg(resultCode);
                    userListerner.onLoginFailed(msg, null);
                    Log.i("cocos", "LoginFail: " + msg);
                }
            }
        });
    }
}
