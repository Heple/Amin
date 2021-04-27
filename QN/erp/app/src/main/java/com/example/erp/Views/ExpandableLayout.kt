package com.example.erp.Views

import android.R
import android.content.Context
import android.util.AttributeSet
import android.view.View
import android.view.animation.Animation
import android.view.animation.Transformation
import android.widget.ImageView
import android.widget.LinearLayout


    class ExpandableLayout(context: Context, attrs: AttributeSet?) : LinearLayout(context, attrs) {
        private val mContext: Context
        private var mHandleView: LinearLayout? = null
        private var mContentView: LinearLayout? = null
        private var mIconExpand: ImageView? = null
        var mContentHeight = 0
        var mTitleHeight = 0
        private var isExpand = false
        private var animationDown: Animation? = null
        private var animationUp: Animation? = null
        override fun onMeasure(widthMeasureSpec: Int, heightMeasureSpec: Int) {
            if (mContentHeight == 0) {
                mContentView!!.measure(widthMeasureSpec, 0)
                mContentHeight = mContentView!!.measuredHeight
            }
            if (mTitleHeight == 0) {
                mHandleView!!.measure(widthMeasureSpec, 0)
                mTitleHeight = mHandleView!!.measuredHeight
            }
            super.onMeasure(widthMeasureSpec, heightMeasureSpec)
        }

//        override fun onFinishInflate() {
//            super.onFinishInflate()
//            mHandleView = findViewById<View>(R.id.ll) as LinearLayout //点击展开的父类布局
//            mContentView = findViewById<View>(R.id.ll_menu) as LinearLayout //要展开的布局
//            mIconExpand = findViewById<View>(R.id.image) as ImageView //图片
//            mHandleView!!.setOnClickListener(ExpandListener()) //展开、隐藏监听
//            //this.mContentView.setOnClickListener(new ExpandListener());
//            mContentView!!.visibility = View.GONE
//        }

//        private inner class ExpandListener : OnClickListener {
//            override fun onClick(paramView: View?) {
//                //clearAnimation是view的方法
//                clearAnimation()
//                if (!isExpand) {
//                    if (animationDown == null) {
//                        animationDown = DropDownAnim(mContentView!!,
//                                mContentHeight, true)
//                        animationDown.setDuration(200) // SUPPRESS CHECKSTYLE
//                    }
//                    startAnimation(animationDown)
//                    mContentView!!.startAnimation(AnimationUtils.loadAnimation(
//                            mContext, R.anim.animalpha))
//                    mIconExpand!!.setImageResource(R.drawable.update_detail_up)
//                    isExpand = true
//                } else {
//                    isExpand = false
//                    if (animationUp == null) {
//                        animationUp = DropDownAnim(mContentView!!,
//                                mContentHeight, false)
//                        animationUp.setDuration(200) // SUPPRESS CHECKSTYLE
//                    }
//                    startAnimation(animationUp)
//                    mIconExpand.setImageResource(R.drawable.update_detail_down)
//                }
//            }
//        }
//
//        internal inner class DropDownAnim
//        /**
//         * 构造方法
//         *
//         * @param targetview
//         * 需要被展现的view
//         * @param vieweight
//         * 目的高
//         * @param isdown
//         * true:向下展开，false:收起
//         */(
//                /** 目标view  */
//                private val view: View,
//                /** 目标的高度  */
//                private val targetHeight: Int,
//                /** 是否向下展开  */
//                private val down: Boolean) : Animation() {
//
//            //down的时候，interpolatedTime从0增长到1，这样newHeight也从0增长到targetHeight
//            override fun applyTransformation(interpolatedTime: Float,
//                                             t: Transformation?) {
//                val newHeight: Int
//                newHeight = if (down) {
//                    (targetHeight * interpolatedTime).toInt()
//                } else {
//                    (targetHeight * (1 - interpolatedTime)).toInt()
//                }
//                view.layoutParams.height = newHeight
//                view.requestLayout()
//                if (view.visibility === View.GONE) {
//                    view.visibility = View.VISIBLE
//                }
//            }
//
//            override fun initialize(width: Int, height: Int, parentWidth: Int,
//                                    parentHeight: Int) {
//                super.initialize(width, height, parentWidth, parentHeight)
//            }
//
//            override fun willChangeBounds(): Boolean {
//                return true
//            }
//
//        }

        init {
            mContext = context
        }
    }