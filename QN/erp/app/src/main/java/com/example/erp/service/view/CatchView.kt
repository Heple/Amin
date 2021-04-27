package com.example.erp.service.view

import com.example.erp.service.enity.Ratchas

interface CatchView:View {
    fun onSuccess(ratch: Ratchas)
    fun onError(str:String)
}