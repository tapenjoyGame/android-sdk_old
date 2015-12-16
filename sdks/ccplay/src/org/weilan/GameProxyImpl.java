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

import com.lion.ccpay.CCPaySdk;
import com.lion.ccpay.CCPaySdk$Stats;
import com.lion.ccpay.login.LoginListener;
import com.lion.ccpay.pay.PayListener;
import com.lion.ccpay.pay.vo.PayResult;
import com.lion.ccpay.user.vo.LoginResult;

public class GameProxyImpl extends GameProxy{
    private Object loginCustomParams;

    public boolean supportLogin() {
        return false;
    }

    public boolean supportCommunity() {
        return false;
    }

    public boolean supportPay() {
        return false;
    }

    public void onCreate(Activity activity) {
        CCPaySdk.getInstance().init(activity);
    }

    public void login(Activity activity,Object customParams) {
        loginCustomParams = customParams;

        CCPaySdk.getInstance().login(activity, new LoginListener() {
            @Override
            public void onComplete(LoginResult result) {
                if (result != null && result.isSuccess) {
                    User u = new User(); // fill User with accountInfo
                    u.userID = Long.toString(accountInfo.getUid());
                    u.token = accountInfo.getSessionId();
                    userListerner.onLoginSuccess(u, loginCustomParams);
                    Toast.makeText(activity, "结果：" + result.toString(), Toast.LENGTH_SHORT).show();
                    // DCAccount.login(result.userId + "");
                } else {
                    userListerner.onLoginFailed("登录失败", loginCustomParams);
                    Toast.makeText(activity, "结果：" + result.toString(), Toast.LENGTH_SHORT).show();
                }
            }
        });
    }

    public void pay(final Activity activity, String ID, String name, String orderID, float price, String callBackInfo, JSONObject roleInfo, PayCallBack payCallBack) { // --TODO what is final
        // 支付 ID：商品ID，name：商品名，orderID：CP订单号，price：金额（单位元），callBackInfo：需要透传给服务器回调，roleInfo：角色信息json，payCallBack：支付回调
        /*
         * local roleInfo = {
         *  id = g_player.entityID,
         *  name = g_player.name,
         *  faction = '',
         *  vip = g_player.vip,
         *  level = g_player.level,
         *  serverID = self.server_id,
         *  raw_username = g_sdk_username,
         *}
         */
        CCPaySdk.getInstance().pay(activity, "100045", "123456789", new PayListener() {

            @Override
            public void onComplete(PayResult result) {
                // TODO Auto-generated method stub

                switch(result.statusCode){
                    case a://success //PayResultCode.PAY_SUCCESS:
                        // 如果成功，接下去需要到自己的服务器查询订单结果
                        Toast.makeText(activity, result.statusCode + "-------" + result.trade_no + "-------" + result.msg, Toast.LENGTH_LONG).show();
                        break;
                    case b://PayResultCode.PAY_ERROR_CANCEL:
                        // 用户取消支付操作
                        Toast.makeText(activity, result.statusCode + "-------" + result.trade_no + "-------" + result.msg, Toast.LENGTH_LONG).show();
                        break;
                    default:
                        // 支付失败，包含错误码和错误消息。
                        // 注意，错误消息需要由游戏展示给用户，错误码可以打印，供调试使用
                        Toast.makeText(activity, result.statusCode + "-------" + result.trade_no + "-------" + result.msg, Toast.LENGTH_LONG).show();
                        break;
                }
            }
        });
    }

    public void onResume(Activity activity) {
        super.onResume(activity);
		CCPaySdk$Stats.onResume(activity);
    }

    public void onPause(Activity activity) {
        super.onPause(activity);
		CCPaySdk$Stats.onPause(activity);
    }

}
