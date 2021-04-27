package com.example.erp.service.view

import com.example.erp.service.enity.News
import com.example.erp.service.enity.Ratchas

interface BbsView:View {
    fun onSuccess(ratch: News)
    fun onError(str:String)
}