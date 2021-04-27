package com.example.erp

import android.annotation.SuppressLint
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.Gravity
import android.view.LayoutInflater
import android.view.View
import android.widget.ExpandableListView
import androidx.drawerlayout.widget.DrawerLayout
import com.example.erp.frament.DrawLeftFrement
import com.example.erp.frament.DrawRightFramet
import com.example.erp.frament.HomeFrement
import com.example.erp.service.enity.News
import com.example.erp.service.enity.Ratchas
import com.example.erp.service.presenter.BbsPrentes
import com.example.erp.service.presenter.NewsPrester
import com.example.erp.service.view.BbsView
import com.example.erp.service.view.NewsView
import kotlinx.android.synthetic.main.activity_context.*
import kotlinx.android.synthetic.main.left_frame.*
import kotlinx.android.synthetic.main.mian_context.*
import kotlin.concurrent.fixedRateTimer

class ContextActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.mian_context)
        fragmentManager.beginTransaction()
                .replace(R.id.draw_item,DrawLeftFrement(this))
                .replace(R.id.main_frame,HomeFrement(this))
                .commit()
        onclick()
    }
    @SuppressLint("WrongConstant")
    fun onclick(){
        right_click_btcv.setOnClickListener {
            fragmentManager.beginTransaction()
                .add(R.id.draw_item,DrawRightFramet())
                .add(R.id.main_frame,HomeFrement(this))
                .commit()
        }
        left_click_btcv.setOnClickListener {
            fragmentManager.beginTransaction()
                .add(R.id.draw_item,DrawLeftFrement(this))
                .add(R.id.main_frame,HomeFrement(this))
                .commit()
        }
        draw_layout.addDrawerListener(object : DrawerLayout.DrawerListener {
            override fun onDrawerStateChanged(newState: Int) {
            }

            override fun onDrawerSlide(drawerView: View, slideOffset: Float) {
            }

            override fun onDrawerClosed(drawerView: View) {
            }

            override fun onDrawerOpened(drawerView: View) {

            }

        })
        var open=false

        open_draw.setOnClickListener {
            if ( draw_layout.isDrawerOpen(Gravity.START)) {
                draw_layout.closeDrawer(Gravity.START)
                open=false
            } else {
                draw_layout.openDrawer(Gravity.START)
                open=true
            }
        }

    }
}