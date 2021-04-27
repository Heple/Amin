package com.example.erp.frament

import android.annotation.SuppressLint
import android.app.Fragment
import android.content.Context
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ExpandableListView
import com.example.erp.R
import com.example.erp.adapter.DiagnosisLeftAdapter
import com.example.erp.adapter.DiagnosisRightAdapter
import com.example.erp.service.enity.DiagnosisReportDetailFist
import com.example.erp.service.enity.DiagnosisReportDetailSecond
import kotlinx.android.synthetic.main.left_frame.*

@SuppressLint("ValidFragment")
class DrawLeftFrement(contexts: Context):Fragment() {
    var contexts=contexts
    var fist= arrayListOf(DiagnosisReportDetailFist("常规设置",R.drawable.settings))
    var two= arrayListOf(arrayListOf(DiagnosisReportDetailSecond(R.drawable.use,"个人配置")))
    var exapandAdapter= DiagnosisLeftAdapter(fist,two)
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?):View{
        return inflater.inflate(R.layout.left_frame,container,false)
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        left_expanded_menus .setGroupIndicator(null)
        left_expanded_menus.setAdapter(exapandAdapter)
        left_expanded_menus.setOnGroupClickListener { parent, v, groupPosition, id -> false
        }
        left_expanded_menus.setOnChildClickListener(ExpandableListView.OnChildClickListener { parent, v, groupPosition, childPosition, id ->  true})

    }
}