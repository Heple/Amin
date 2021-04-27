package com.example.erp.service.view

import com.example.erp.service.enity.News
import com.example.erp.service.enity.Ratchas

interface NewsView:View {
    fun onSuccess(news:News)
    fun onError(str: String)
}