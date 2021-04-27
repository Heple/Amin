package com.example.erp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.LinearLayout
import com.example.erp.unit.getAgentWeb
import com.just.library.ChromeClientCallbackManager
import kotlinx.android.synthetic.main.activity_web.*
import kotlinx.android.synthetic.main.mian_context.*

class WebActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_web)
        var Str=intent.getStringExtra("t1")
        Str.getAgentWeb(this,web_context,LinearLayout.LayoutParams(-1,-1))
    }
    private val receivedTitleCallback =
        ChromeClientCallbackManager.ReceivedTitleCallback { _, title ->
            title?.let {
                toolbar.title = it
            }
        }
}