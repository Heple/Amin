package com.example.erp.frament

import android.app.Fragment
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ExpandableListView
import androidx.constraintlayout.widget.Constraints.TAG
import com.example.erp.R
import com.example.erp.adapter.DiagnosisRightAdapter
import com.example.erp.service.enity.DiagnosisReportDetailFist
import com.example.erp.service.enity.DiagnosisReportDetailSecond
import kotlinx.android.synthetic.main.left_frame.*

class DrawRightFramet: Fragment() {
    lateinit var f1:DiagnosisReportDetailFist
    lateinit var f2:DiagnosisReportDetailSecond
    var strlist= arrayListOf("广告管理控制台","落地页管理","插件管理","客服管理","广告报表","广告资质","广告监测","安全管理","复制统计","ipv4转ipv6")
    var imglist= arrayListOf(R.drawable.r1,R.drawable.r2,R.drawable.r3,R.drawable.r4,R.drawable.r5,R.drawable.r6,R.drawable.r7,R.drawable.r8,R.drawable.r9,R.drawable.r10)
     var fist=ArrayList<DiagnosisReportDetailFist>()
    var temp=ArrayList<DiagnosisReportDetailSecond>()
     var childmulist=ArrayList<DiagnosisReportDetailSecond>()
     var two=ArrayList<ArrayList<DiagnosisReportDetailSecond>>()
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        return inflater.inflate(R.layout.left_frame,container,false)
    }
    fun stadata(){
        for (i in 0..9){
            f1= DiagnosisReportDetailFist(strlist[i],imglist[i])
            fist.add(f1)
        }
        two= arrayListOf(arrayListOf(),
        arrayListOf(DiagnosisReportDetailSecond(R.drawable.c_1_1,"落地页列表"), DiagnosisReportDetailSecond(R.drawable.c_1_2,"内容管理")),
                arrayListOf(DiagnosisReportDetailSecond(R.drawable.r3,"插件管理")),
                arrayListOf(),
                arrayListOf(DiagnosisReportDetailSecond(R.drawable.c_3_1,"广告报表控制台"),DiagnosisReportDetailSecond(R.drawable.c_3_2,"绑定控制台"),DiagnosisReportDetailSecond(R.drawable.c_3_3,"账户列表"),DiagnosisReportDetailSecond(R.drawable.c_3_4,"市场数据分析"),DiagnosisReportDetailSecond(R.drawable.c_3_5,"时间段数据分析"),DiagnosisReportDetailSecond(R.drawable.c_3_6,"搜索词数据分析"),DiagnosisReportDetailSecond(R.drawable.c_3_7,"地域数据分析")),
                arrayListOf(),
                arrayListOf(DiagnosisReportDetailSecond(R.drawable.c_4_1,"广告数据实况"),DiagnosisReportDetailSecond(R.drawable.c_4_2,"广告记录"),DiagnosisReportDetailSecond(R.drawable.c_4_3,"复制记录"),DiagnosisReportDetailSecond(R.drawable.c_4_4,"客服加粉记录"),DiagnosisReportDetailSecond(R.drawable.c_4_5,"百度关键词同步")),
                arrayListOf(DiagnosisReportDetailSecond(R.drawable.c_5_1,"恶意ip管理"),DiagnosisReportDetailSecond(R.drawable.c_5_2,"放刷屏关键词")),
                arrayListOf(DiagnosisReportDetailSecond(R.drawable.c_6,"复制搜索词统计"),DiagnosisReportDetailSecond(R.drawable.c_6,"复制落地页排行"),DiagnosisReportDetailSecond(R.drawable.c_6,"复制地区统计"),DiagnosisReportDetailSecond(R.drawable.c_6,"复制来源统计"),DiagnosisReportDetailSecond(R.drawable.c_6,"复制微信号统计")),
                arrayListOf()
        )
    }
    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        stadata()
        var exapandAdapter= DiagnosisRightAdapter(fist,two)
        left_expanded_menus .setGroupIndicator(null)
        left_expanded_menus.setAdapter(exapandAdapter)
        left_expanded_menus.setOnGroupClickListener { parent, v, groupPosition, id ->
            if (groupPosition==0||groupPosition==3||groupPosition==5||groupPosition==9){
                true
            }else false
        }
        left_expanded_menus.setOnChildClickListener(ExpandableListView.OnChildClickListener { parent, v, groupPosition, childPosition, id ->  true})
        left_expanded_menus.setOnGroupExpandListener {
            var count=left_expanded_menus.expandableListAdapter.groupCount
            for(i in 0..count-1){
                if (it!=i){
                    left_expanded_menus.collapseGroup(i)
                }
            }
        }
    }
}