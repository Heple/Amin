package com.example.erp.service.enity

import android.text.format.Time

data class PerFileData(var total:Int,var rows: List<Rows>){
    data class Rows(var admin_id:Int,
                    var company_id:Int,
                    var content:String,
                    var createtime:Long,
                    var id:Int,
                    var ip:String,
                    var title:String,
                    var url:String,
                    var useragent:String,
                    var username:String)
}