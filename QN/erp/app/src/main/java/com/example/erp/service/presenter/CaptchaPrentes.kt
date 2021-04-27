package com.example.erp.service.presenter

import android.content.Context
import android.content.Intent
import com.example.erp.service.enity.Ratchas
import com.example.erp.service.manager.DataManager
import com.example.erp.service.view.CatchView
import com.example.erp.service.view.View
import rx.Observer
import rx.android.schedulers.AndroidSchedulers
import rx.schedulers.Schedulers
import rx.subscriptions.CompositeSubscription

class CaptchaPrentes(mContext: Context?):Presentes {

    private var manager: DataManager? = null
    private var mCompositeSubscription: CompositeSubscription? = null
    private var mContext: Context? = null
    private var mCatvhView: CatchView? = null
    private var mRatchas: Ratchas? = null
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
        mCatvhView = view as CatchView?
    }

    fun attachIncomingIntent(intent: Intent?) {}
    fun getCaptcha(__token__:String,username:String,password:String,captcha:String) {
        mCompositeSubscription!!.add(manager!!.userLogin(__token__, username, password, captcha)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(object : Observer<Ratchas> {
                    override fun onCompleted() {
                        if (mRatchas != null) {
                            mCatvhView!!.onSuccess(mRatchas!!)
                        }
                    }
                   override fun onError(e: Throwable) {
                        e.printStackTrace()
                       mCatvhView!!.onError(e.message!!)
                    }
                   override fun onNext(ratchas: Ratchas?) {
                       mRatchas = ratchas
                    }
                })
        )
    }
}