package com.example.erp.unit

import android.app.Activity
import android.view.ViewGroup
import com.just.library.AgentWeb
import com.just.library.ChromeClientCallbackManager

fun String.getAgentWeb(
    activity: Activity, webContent: ViewGroup,
    layoutParams: ViewGroup.LayoutParams
) = AgentWeb.with(activity)
        .setAgentWebParent(webContent, layoutParams)
        .useDefaultIndicator()
        .defaultProgressBarColor()
       // .setReceivedTitleCallback(receivedTitleCallback)
        .createAgentWeb()//
        .ready()
        .go(this)!!