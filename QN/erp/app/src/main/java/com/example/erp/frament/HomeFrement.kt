package com.example.erp.frament

import android.annotation.SuppressLint
import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.FrameLayout
import androidx.fragment.app.Fragment
import com.example.erp.R
import com.example.erp.WebActivity
import com.example.erp.service.enity.News
import com.example.erp.service.presenter.BbsPrentes
import com.example.erp.service.presenter.NewsPrester
import com.example.erp.service.view.BbsView
import com.example.erp.service.view.NewsView
import kotlinx.android.synthetic.main.activity_context.*

@SuppressLint("ValidFragment")
class HomeFrement(context: Context): android.app.Fragment() {
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {
        return inflater.inflate(R.layout.activity_context,container,false)
    }


    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        startLogin()
        textOnClick()
    }
    var intent= Intent(context,WebActivity::class.java)
    var newsPrester = NewsPrester(context)
    var bbsprent= BbsPrentes(context)
    var newsView = object : NewsView {
        override fun onSuccess(news: News) {
            lodenewtext(news)
        }
        override fun onError(str: String) {
            Log.i("ContextActivity","--------------"+str)
        }
    }
    var bbsView = object : BbsView {
        override fun onSuccess(news: News) {
            lodebbstext(news)
        }
        override fun onError(str: String) {
            Log.i("ContextActivity","--------------"+str)
        }
    }
    fun startLogin() {
        newsPrester.onCreate()
        newsPrester.attachView(newsView)
        newsPrester.getNews()
        bbsprent.onCreate()
        bbsprent.attachView(bbsView)
        bbsprent.getNews()
    }
    fun lodenewtext(news: News){
        notif_1.text=news.data[0].title
        notif_2.text=news.data[1].title
        notif_3.text=news.data[2].title
        notif_4.text=news.data[3].title
    }
    fun lodebbstext(news: News){
        quest_1.text=news.data[0].title
        quest_2.text=news.data[1].title
        quest_3.text=news.data[2].title
        quest_4.text=news.data[3].title
    }
    fun textOnClick(){
        notif_1.setOnClickListener {
            intent.putExtra("t1","http://forum.lm12301.com/?thread-2.htm")
            startActivity(Intent(intent)) }
        notif_2.setOnClickListener {
            intent.putExtra("t1","http://forum.lm12301.com/?thread-1.htm")
            startActivity(Intent(intent))
        }
        notif_3.setOnClickListener {
            intent.putExtra("t1","http://forum.lm12301.com/?thread-3.htm")
            startActivity(Intent(intent))
        }
        notif_4.setOnClickListener {
            intent.putExtra("t1","http://forum.lm12301.com/?thread-4.htm")
            startActivity(Intent(intent))
        }
        quest_1.setOnClickListener {
            intent.putExtra("t1","http://forum.lm12301.com/?thread-15.htm")
            startActivity(Intent(intent))
        }
        quest_2.setOnClickListener {
            intent.putExtra("t1","http://forum.lm12301.com/?thread-14.htm")
            startActivity(Intent(intent))
        }
        quest_3.setOnClickListener {
            intent.putExtra("t1","http://forum.lm12301.com/?thread-13.htm")
            startActivity(Intent(intent))
        }
        quest_4.setOnClickListener {
            intent.putExtra("t1","http://forum.lm12301.com/?thread-12.htm")
            startActivity(Intent(intent))
        }
        more_fist.setOnClickListener {
            intent.putExtra("t1","http://forum.lm12301.com/")
            startActivity(Intent(intent))
        }
        more_two.setOnClickListener {
            intent.putExtra("t1","http://forum.lm12301.com/")
            startActivity(Intent(intent))
        }
    }
}