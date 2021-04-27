package com.example.erp.service


import com.example.erp.service.enity.News
import com.example.erp.service.enity.PerFileData
import com.example.erp.service.enity.Ratchas
import org.json.JSONObject
import retrofit2.http.*
import rx.Observable


interface RetrofitService {
    @Headers("cookie:PHPSESSID=11", "x-requested-with:XMLHttpRequest")

    @POST("lvmeng.php/index/login")
    @FormUrlEncoded
    fun userLogin(@Field("__token__")__token__:String,
                  @Field("username")username:String,
                  @Field("password")password:String,
                  @Field("captcha")captcha:String): Observable<Ratchas>

    @Headers("cookie:PHPSESSID=10", "x-requested-with:XMLHttpRequest")
    @POST("lvmeng.php/dashboard/news")
    fun Nuews(): Observable<News>

    @Headers("cookie:PHPSESSID=10", "x-requested-with:XMLHttpRequest")
    @POST("lvmeng.php/dashboard/bbs")
    fun Bbs(): Observable<News>

    @Headers("cookie:PHPSESSID=10", "x-requested-with:XMLHttpRequest")
    @GET("lvmeng.php/general/profile/index")
    fun Prefile(@Query("sort")sort:String,
                @Query("order")order:String,
                @Query("offset")offset:Int,
                @Query("limit")limit:Int,
                @Query("_")_t:String):Observable<PerFileData>
}