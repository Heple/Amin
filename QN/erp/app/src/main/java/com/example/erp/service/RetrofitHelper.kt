package com.example.erp.service

import android.content.Context
import com.google.gson.GsonBuilder
import okhttp3.OkHttpClient
import retrofit2.Retrofit
import retrofit2.adapter.rxjava.RxJavaCallAdapterFactory
import retrofit2.converter.gson.GsonConverterFactory



class RetrofitHelper private constructor(mContext: Context) {
    private val mCntext: Context
    var client = OkHttpClient()
    var factory = GsonConverterFactory.create(GsonBuilder().setLenient().create())
    private var mRetrofit: Retrofit? = null
    private fun init() {
        resetApp()
    }

    private fun resetApp() {
        mRetrofit = Retrofit.Builder()
            .baseUrl("https://erp.lm12301.com/")
            .client(client)
            .addConverterFactory(factory)
            .addCallAdapterFactory(RxJavaCallAdapterFactory.create())
            .build()
    }
    val server: RetrofitService
        get() = mRetrofit!!.create(RetrofitService::class.java)
    companion object {
        private var instance: RetrofitHelper? = null
        fun getInstance(context: Context): RetrofitHelper? {
            if (instance == null) {
                instance = RetrofitHelper(context)
            }
            return instance
        }
    }
    init {
        mCntext = mContext
        init()
    }
}