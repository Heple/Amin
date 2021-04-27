package com.example.erp.service.presenter

import android.content.Context
import android.content.Intent
import com.example.erp.service.enity.News
import com.example.erp.service.enity.Ratchas
import com.example.erp.service.manager.DataManager
import com.example.erp.service.view.BbsView
import com.example.erp.service.view.CatchView
import com.example.erp.service.view.NewsView
import com.example.erp.service.view.View
import rx.Observer
import rx.android.schedulers.AndroidSchedulers
import rx.schedulers.Schedulers
import rx.subscriptions.CompositeSubscription

class BbsPrentes(mContext: Context):Presentes {
    private var manager: DataManager? = null
    private var mCompositeSubscription: CompositeSubscription? = null
    private var mContext: Context? = null
    private var newsView: BbsView? = null
    private var mNews: News? = null
    init {
        this.mContext = mContext
    }
    override fun onCreate() {
        manager = mContext?.let { DataManager(it) }
        mCompositeSubscription = CompositeSubscription()
    }

    override fun onStop() {
        if (mCompositeSubscription!!.hasSubscriptions()) {
            mCompositeSubscription!!.unsubscribe()
        }
    }

    override fun attachView(view: View) {
        newsView = view as BbsView?
    }

    fun attachIncomingIntent(intent: Intent?) {}
    fun getNews() {
        mCompositeSubscription!!.add(manager!!.Bbs()
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(object : Observer<News> {
                    override fun onCompleted() {
                        if (mNews != null) {
                            newsView!!.onSuccess(mNews!!)
                        }
                    }
                    override fun onError(e: Throwable) {
                        e.printStackTrace()
                        newsView!!.onError(e.message!!)
                    }
                    override fun onNext(news: News?) {
                        mNews = news
                    }
                })
        )
    }
}