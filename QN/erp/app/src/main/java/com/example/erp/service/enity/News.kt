package com.example.erp.service.enity

import java.io.Serializable

data class News(val code:Int,val msg:String,val data:List<Data>,val url: String){
   data class Data(val id:Int,val title:String,val url:String)
}