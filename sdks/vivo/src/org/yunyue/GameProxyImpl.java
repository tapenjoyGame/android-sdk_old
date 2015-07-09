package org.yunyue;

import java.util.UUID;
import org.json.JSONObject;
import org.json.JSONException;
import java.text.DecimalFormat;

import android.app.Activity;
import android.content.Intent;
import android.content.Context;
import android.util.Log;
import android.os.Handler;
import android.os.Bundle;
import android.os.Message;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLEncoder;


import com.vivo.account.base.activity.LoginActivity;
import com.bbk.payment.PaymentActivity;

class ProductInfo {
    public String productName;
    public String productDesc;
    public String price;
    public String userName;
    public String goodsID;
    public String orderID;
    public String callBackInfo;

    public ProductInfo(String productName, String productDesc, String price, String userName, String goodsID, String orderID, String callBackInfo) {
        this.productName = productName;
        this.productDesc = productDesc;
        this.price = price;
        this.userName = userName;
        this.goodsID = goodsID;
        this.orderID = orderID;
        this.callBackInfo = callBackInfo;
    }
}

public class GameProxyImpl extends GameProxy {

    public final static String KEY_LOGIN_RESULT = "LoginResult";
	public final static String KEY_OPENID = "openid";
	public final static String KEY_AUTHTOKEN = "authtoken";
	public final static String KEY_SHOW_TEMPLOGIN = "showTempLogin";
    private static final int REQUEST_CODE_LOGIN = 1;
    private static final int REQUEST_CODE_PAY = 1;
    private static final String appid = "${APPID}";
    private static final int START_PAY = 1;
    private String mOrderInfo;
    private Activity currentActivity;
    private ProductInfo productInfo;

    Handler mHandler = new Handler()
    {
        public void handleMessage( android.os.Message msg )
        {
            JSONObject jOrder = new JSONObject(mOrderInfo);
            if (msg.what == START_PAY)
            {
                Bundle localBundle = new Bundle();
                localBundle.putString("transNo", jOrder.getString("orderNumber"));// 交易流水号，由订单推送接口返回
                localBundle.putString("accessKey", jOrder.getString("access_token"));// 由订单推送接口返回
                localBundle.putString("productName", productInfo.productName);//商品名称
                localBundle.putString("productDes", productInfo.productDesc);//商品描述
                localBundle.putLong("price", productInfo.price);//价格,单位为分（1000即10.00元）
                localBundle.putString("appId", appid);// appid为vivo开发者平台中生成的App ID

                // 以下为可选参数，能收集到务必填写，如未填写，掉单、用户密码找回等问题可能无法解决。
                //localBundle.putString("blance", "100元宝");
                //localBundle.putString("vip", "vip2");
                //localBundle.putInt("level", 35);
                //localBundle.putString("party", "工会");
                //localBundle.putString("roleId", "角色id");
                //localBundle.putString("roleName", "角色名称");
                //localBundle.putString("serverName", "区服信息");
                localBundle.putString("extInfo", productInfo.callBackInfo);
                localBundle.putBoolean("logOnOff", false);// CP在接入过程请传true值,接入完成后在改为false, 传true会在支付SDK打印大量日志信息	 
                Intent target = new Intent(currentActivity, PaymentActivity.class);
                target.putExtra("payment_params", localBundle);
                currentActivity.startActivityForResult(target, REQUEST_CODE_PAY);
            }
        };
    };

    public void applicationInit(Activity activity) {
        currentActivity = activity;
    }

    public boolean supportLogin() {
        return true;
    }

    //public boolean supportCommunity() {
    //    return true;
    //}

    public boolean supportPay() {
        return true;
    }

    public void login(Activity activity, Object customParams) {
        Intent loginIntent = new Intent(activity, LoginActivity.class);
        activity.startActivityForResult(loginIntent, REQUEST_CODE_LOGIN);
    }

    public void pay(Activity activity, String ID, String name, String orderID, float price, String callBackInfo, JSONObject roleInfo, PayCallBack payCallBack) {

        DecimalFormat df = new DecimalFormat("0.00");
        productInfo = new ProductInfo(name, "元宝", df.format(price),
                "", ID, orderID, callBackInfo);

        new Thread(new Runnable()
            {
                @ Override
                public void run( )
                {
                    getOrderInfo(productInfo);
                }
            }).start();
    }

    /** 支付前去服务端创建订单 */
    private void getOrderInfo( ProductInfo productInfo )
    {
        String sUrl = ((poem)currentActivity).getMetaData("create_order_url");
        try
        {
            URL url = new URL(sUrl);
            HttpURLConnection connection = (HttpURLConnection) url
                .openConnection();
            connection.setRequestMethod("POST");
            connection.setRequestProperty("Content-type",
                    "application/x-www-form-urlencoded");
            connection.setDoOutput(true);// 是否输入参数
            StringBuffer params = new StringBuffer();
            params.append("&returnJson=");
            params.append(enCode("{\"channel\": \"vivo\", \"open_id\": \"\", \"user_name\": \"\", \"access_token\": \"\" }"));
            params.append("&productName=");
            params.append(enCode(productInfo.productName));
            params.append("&description=");
            params.append(enCode(productInfo.productDesc));
            params.append("&amount=");
            params.append(enCode(productInfo.price));
            params.append("&orderid=");
            params.append(enCode(productInfo.orderID));
            params.append("&cpPrivateInfo=");
            params.append(enCode(productInfo.callBackInfo));
            Log.d("MyView", "getOrderInfo: " + params.toString());
            byte[] bytes = params.toString().getBytes();
            connection.connect();
            connection.getOutputStream().write(bytes);
            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(connection.getInputStream()));
            StringBuffer readbuff = new StringBuffer();
            String lstr = null;
            while ((lstr = reader.readLine()) != null)
            {
                readbuff.append(lstr);
            }
            Log.i("MyView", "getOrderInfo: " + readbuff.toString());
            connection.disconnect();
            reader.close();
            mOrderInfo = readbuff.toString();
            Log.i("MyView", "getOrderInfo: " + mOrderInfo);
            mHandler.sendEmptyMessage(START_PAY);

        } catch (MalformedURLException e)
        {
            e.printStackTrace();
        } catch (JSONException e)
        {
            e.printStackTrace();
        } catch (IOException e)
        {
            e.printStackTrace();
        }
    }

    private String enCode( String value )
    {
        String enCodeValue = null;
        try
        {
            enCodeValue = URLEncoder.encode(value, "UTF-8");
        } catch (UnsupportedEncodingException e)
        {
            e.printStackTrace();
        }
        return enCodeValue;
    }

    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
		Log.d("sdk", "MainActivity, onActivityResult,requestCode="+requestCode+", resultCode="+resultCode);
		if(requestCode == REQUEST_CODE_LOGIN){
			if(resultCode == Activity.RESULT_OK){
				String loginResult = data.getStringExtra(KEY_LOGIN_RESULT);
				JSONObject loginResultObj;
				try {
					loginResultObj = new JSONObject(loginResult);
					String name = loginResultObj.getString(KEY_NAME);
					String openid = loginResultObj.getString(KEY_OPENID);
					String authtoken = loginResultObj.getString(KEY_AUTHTOKEN);
                    User u = new User();
                    u.userID = openid;
                    u.token = authtoken;
                    userListerner.onLoginSuccess(u, null);
				} catch (JSONException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} 
//				Toast.makeText(mContext, loginResult, Toast.LENGTH_SHORT).show();
				Log.d("sdk", "loginResult="+loginResult);
			}
		}
        else if (requestCode == REQUEST_CODE_PAY) {
            //
        }
	}
}
