package com.example.erp

import android.app.Dialog
import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.ImageView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.bumptech.glide.Glide
import com.bumptech.glide.load.engine.DiskCacheStrategy
import com.bumptech.glide.load.model.GlideUrl
import com.bumptech.glide.load.model.LazyHeaders
import com.example.erp.service.enity.Ratchas
import com.example.erp.service.presenter.CaptchaPrentes
import com.example.erp.service.view.CatchView


class MainActivity : AppCompatActivity() {
    var captchaPrentes = CaptchaPrentes(this)
    lateinit var dialog_view: View
    lateinit var username: EditText
    lateinit var password: EditText
    lateinit var captcha: EditText
    lateinit var login: Button
    lateinit var code: ImageView
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        startLogin()
        Widgetinit()
        loginview()
        WidgetonClick()
    }

    fun loginview() {
        val dialog = Dialog(this, R.style.my_dialog)
        dialog.setContentView(dialog_view)
        dialog.setCancelable(false)
        val window = dialog.window
        val lp = window!!.attributes
        lp.dimAmount = 0.0f
        window.setAttributes(lp)
        window.setWindowAnimations(R.style.dialog_anim);
        startcode()
        dialog.show()
    }
    fun startcode() {
        val gu = GlideUrl("https://erp.lm12301.com/index.php?s=/captcha", LazyHeaders.Builder()
                .addHeader("cookie", "PHPSESSID=11").build())
        Glide.with(this)
                .load(gu)
            .skipMemoryCache(true)
                .diskCacheStrategy(DiskCacheStrategy.NONE)
                .into(code)
    }

    var catchView = object : CatchView {
        override fun onSuccess(ratch: Ratchas) {
            Log.i("Mainivity",ratch.msg)
            if (ratch.code == 1) {
                startActivity(Intent(this@MainActivity, ContextActivity::class.java))
                overridePendingTransition(R.anim.activity_anim_enter,R.anim.activity_anim_exit)
            }
        }
        override fun onError(str: String) {
            Toast.makeText(this@MainActivity, "登录失败" + str, Toast.LENGTH_LONG).show()
            startcode()
        }
    }
    fun Widgetinit() {
        dialog_view = LayoutInflater.from(this).inflate(R.layout.login, null)
        username = dialog_view.findViewById<EditText>(R.id.acction)
        password = dialog_view.findViewById<EditText>(R.id.password)
        captcha = dialog_view.findViewById<EditText>(R.id.code)
        code = dialog_view.findViewById<ImageView>(R.id.code_img)
        login = dialog_view.findViewById(R.id.login)
    }
    fun WidgetonClick() {
        login.setOnClickListener {
            captchaPrentes.onCreate()
            captchaPrentes.attachView(catchView)
            captchaPrentes.getCaptcha("", username.text.toString() + "", password.text.toString(), captcha.text.toString())
        }
        code.setOnClickListener {
            Toast.makeText(this,"点击了",Toast.LENGTH_LONG).show()
            startcode()
        }
    }

    fun startLogin() {
        captchaPrentes.onCreate()
        captchaPrentes.attachView(catchView)
        captchaPrentes.getCaptcha("", "", "", "")
    }
}