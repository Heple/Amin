package com.example.erp.service.manager

import android.content.Context
import com.example.erp.service.RetrofitHelper

import com.example.erp.service.RetrofitService
import com.example.erp.service.enity.News
import com.example.erp.service.enity.Ratchas
import com.example.erp.service.presenter.BbsPrentes
import org.json.JSONObject
import rx.Observable
import java.util.*


class DataManager(context: Context) {
    private val mRetrofitService: RetrofitService
    fun userLogin(
            __token__:String,username:String,password:String,captcha:String
    ): Observable<Ratchas> {
        return mRetrofitService.userLogin(__token__, username, password, captcha)
    }
    fun _News():Observable<News>{
        return mRetrofitService.Nuews()
    }
    fun Bbs():Observable<News>{
        return mRetrofitService.Bbs()
    }
    init {
        mRetrofitService = RetrofitHelper.getInstance(context)!!.server
    }
}