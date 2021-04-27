package com.example.erp.adapter

import android.content.ContentValues.TAG
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.BaseExpandableListAdapter
import android.widget.ImageView
import android.widget.TextView
import com.example.erp.R
import com.example.erp.service.enity.DiagnosisReportDetailFist
import com.example.erp.service.enity.DiagnosisReportDetailSecond
import kotlinx.android.synthetic.main.group_item.view.*
import kotlinx.android.synthetic.main.child_item.view.*


class DiagnosisRightAdapter : BaseExpandableListAdapter {
    var diagnosisReportDetailFirst: MutableList<DiagnosisReportDetailFist> = mutableListOf()
    var diagnosisReportDetailSecond: ArrayList<ArrayList<DiagnosisReportDetailSecond>> = arrayListOf()
    lateinit var groupViewHolder:GroupViewHolder
    lateinit var childViewHolder:ChildViewHolder
        constructor(
                diagnosisReportDetailFirst: ArrayList<DiagnosisReportDetailFist>,
                diagnosisReportDetailSecond: ArrayList<ArrayList<DiagnosisReportDetailSecond>>
        ) : super() {
            this.diagnosisReportDetailFirst = diagnosisReportDetailFirst
            this.diagnosisReportDetailSecond = diagnosisReportDetailSecond
        }

        override fun getGroupCount(): Int {
            return diagnosisReportDetailFirst.size
        }


        override fun getChildrenCount(groupPosition: Int): Int {
                return diagnosisReportDetailSecond.get(groupPosition).size
            }


        override fun getGroup(groupPosition: Int): Any {
            return diagnosisReportDetailFirst.get(groupPosition)
        }


        override fun getChild(groupPosition: Int, childPosition: Int): Any? {
                return diagnosisReportDetailSecond.get(groupPosition).get(childPosition)
        }

        override fun getGroupId(groupPosition: Int): Long {
            return groupPosition.toLong()
        }
        override fun getChildId(groupPosition: Int, childPosition: Int): Long {
            return childPosition.toLong()
        }

        override fun hasStableIds(): Boolean {
            return true
        }

        override fun getGroupView(
                groupPosition: Int,
                isExpanded: Boolean,
                convertView: View?,
                parent: ViewGroup?
        ): View {
            var mconvertView = convertView
                if (convertView == null) {
                    mconvertView = LayoutInflater.from(parent?.context).inflate(R.layout.group_item, parent, false)
                    groupViewHolder = GroupViewHolder(mconvertView!!)
                    mconvertView.tag = groupViewHolder
                } else {
                    groupViewHolder = mconvertView!!.tag as GroupViewHolder
                }
                groupViewHolder.group_text?.text = diagnosisReportDetailFirst[groupPosition].group_text
                groupViewHolder.group_img?.setImageResource(diagnosisReportDetailFirst[groupPosition].group_img)
            if (groupPosition==0||groupPosition==3||groupPosition==5||groupPosition==9){
                groupViewHolder.group_all?.setImageResource(R.drawable.null_back)
            }else{
                if (isExpanded) {
                    groupViewHolder.group_all?.setImageResource(R.drawable.bottom_item)
                } else {
                    groupViewHolder.group_all?.setImageResource(R.drawable.item_image)
            }}
            return mconvertView!!
        }

        override fun getChildView(
                groupPosition: Int,
                childPosition: Int,
                isLastChild: Boolean,
                convertView: View?,
                parent: ViewGroup?
        ): View? {
            var mconvertView = convertView
                if (convertView == null) {
                    mconvertView = LayoutInflater.from(parent?.context).inflate(R.layout.child_item, parent, false)
                    childViewHolder = ChildViewHolder(mconvertView!!)
                    mconvertView.tag = childViewHolder
                } else {
                    childViewHolder = mconvertView?.tag as ChildViewHolder
                }
                childViewHolder.child_test?.text = diagnosisReportDetailSecond[groupPosition][childPosition].child_str
                childViewHolder.child_img?.setImageResource(diagnosisReportDetailSecond[groupPosition][childPosition].child_img)
            return mconvertView
        }
    lateinit var btck:btonclick
    interface btonclick{
        fun onclick(view: View)
    }
        override fun isChildSelectable(groupPosition: Int, childPosition: Int): Boolean {
            return true
        }


        inner class GroupViewHolder(view:View) {
            var group_text: TextView? = null
            var group_img: ImageView? = null
            var group_all: ImageView? = null
            init {
                group_text = view.draw_text
                group_img = view.draw_left_image
                group_all = view.draw_image_rote
            }
        }
    inner class GroupNullViewHolder(view:View) {
        var group_text: TextView? = null
        var group_img: ImageView? = null
        init {
            group_text = view.draw_text
            group_img = view.draw_left_image
        }
    }
        inner  class ChildViewHolder(view:View){
            var child_test: TextView? = null
            var child_img: ImageView? = null
            init {
                child_test = view.two_item
                child_img = view.two_img
            }
        }

    }