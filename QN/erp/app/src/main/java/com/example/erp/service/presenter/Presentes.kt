package com.example.erp.service.presenter

import com.example.erp.service.view.View

interface Presentes {
    fun onCreate()
    fun onStop()
    fun attachView(view:View)
}