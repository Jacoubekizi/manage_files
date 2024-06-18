<?php

use App\Http\Controllers\Api\ApplicationRatingController;
use App\Http\Controllers\Api\AuthController;
use App\Http\Controllers\Api\CountryController;
use App\Http\Controllers\Api\CouponController;
use App\Http\Controllers\Api\OfferController;
use App\Http\Controllers\Api\FavoriteController;
use App\Http\Controllers\Api\HomePageController;
use App\Http\Controllers\Api\MinisurviceController;
use App\Http\Controllers\Api\OtpController;
use App\Http\Controllers\Api\PaymentController;
use App\Http\Controllers\Api\PointController;
use App\Http\Controllers\Api\QuestionAnswerController;
use App\Http\Controllers\Api\RatingController;
use App\Http\Controllers\Api\RegionController;
use App\Http\Controllers\Api\ReservationController;
use App\Http\Controllers\Api\Search;
use App\Http\Controllers\Api\SettingController;
use App\Http\Controllers\Api\SubsurviceController;
use App\Http\Controllers\Api\SurviceController;
use App\Http\Controllers\Api\TransactionController;
use App\Http\Controllers\Api\WelcomeController;
use Illuminate\Support\Facades\Route;

//use App\Http\Controllers\PushNotificationController;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/


// auth route
Route::group(['middleware' => 'api', 'prefix' => 'auth'], function ($router) {
    Route::post('/login', [AuthController::class, 'login']);
    Route::post('/register', [AuthController::class, 'register']);
    Route::post('/verifyotp', [OtpController::class, 'verifyOtpForRegistration']);
    Route::post('/resendotp', [OtpController::class, 'sendOtp']);
    Route::post('/startpasswordreset', [AuthController::class, 'startPasswordReset']);
    Route::post('/verifyotpforpassword', [OtpController::class, 'verifyOtpForPasswordReset']);
    Route::post('/setnewpassword', [AuthController::class, 'setNewPassword']);
    Route::post('/logout', [AuthController::class, 'logout']);
    Route::post('/refresh', [AuthController::class, 'refresh']);
    Route::get('/user-profile', [AuthController::class, 'userProfile']);
    Route::post('/edit-profile', [AuthController::class, 'editinfo']);
    Route::post('/updatepassword/{userid}', [AuthController::class, 'updatePassword']);
});


//home page
Route::get('/home-page', [HomePageController::class, 'index']);


//country route
Route::get('/country-list', [CountryController::class, 'index']);


//setting route
Route::get('/setting', [SettingController::class, 'index']);
Route::post('setting/addsetting', [SettingController::class, 'store']);
Route::post('setting/editsetting/{id}', [SettingController::class, 'update']);
Route::post('setting/deletesetting/{id}', [SettingController::class, 'delete']);


//welcome route
Route::get('/allwelcome', [WelcomeController::class, 'index']);
Route::get('/welcome/{id}', [WelcomeController::class, 'show']);


//survice
Route::get('/allsurvices', [SurviceController::class, 'index']);
Route::get('/survice/{id}', [SurviceController::class, 'show']);
Route::get('/getAllsubsurvices/{id}', [SurviceController::class, 'getAllsubsurvices']);
Route::get('/getAllminisurvices/{id}', [SurviceController::class, 'getAllminisurvices']);


//subsurvice
Route::get('/allsubsurvices', [SubsurviceController::class, 'index']);
Route::get('/subsurvice/{id}', [SubsurviceController::class, 'show']);
Route::get('/allminisurvicesforsubsurvice/{id}', [SubsurviceController::class, 'getAllminisurvices']);


//mini survice
Route::get('/allminisurvices', [MinisurviceController::class, 'index']);
Route::get('/minisurvice/{id}', [MinisurviceController::class, 'show']);
Route::get('/popularminisurvice', [MinisurviceController::class, 'popularminisurvice']);


//search
Route::get('/searchminisurvice/{search}', [Search::class, 'searchminisurvice']);
Route::post('/specialsearch', [Search::class, 'specialsearch']);
Route::get('/searcharchive/{id}', [Search::class, 'searcharchive']);


//rating
Route::controller(RatingController::class)->middleware('jwt.verify')->group(function () {
    Route::post('/rating/store', 'store');
    Route::POST('/rating/edit/{id}', 'edit');
    Route::get('/rating/{minisurvice_id}', 'show')->withoutMiddleware('jwt.verify');
    Route::get('/rating/user/{user_id}', 'userrating')->withoutMiddleware('jwt.verify');
});


//region
Route::get('/region', [RegionController::class, 'index']);


//coupon
Route::get('/coupon', [CouponController::class, 'index']);
Route::get('/coupon/{coupon}', [CouponController::class, 'checkcoupon']);
Route::get('/endcoupon', [CouponController::class, 'endcoupon']);


//reservations
Route::controller(ReservationController::class)->middleware('jwt.verify')->group(function () {
    Route::post('/reservation/store', 'store');
    Route::post('/reservation/delete/{id}', 'delete');
    Route::get('/reservation/myreservation/{user_id}', 'myreservation');
    Route::get('/reservation/mypastreservation/{user_id}', 'mypastreservation');
    Route::get('/reservation/mypendreservation/{user_id}', 'mypendreservation');
});

//payment
Route::middleware('jwt.verify')->group(function () {

    Route::get('/reservation/pay/{id}', [PaymentController::class, 'processReservationPayment']);
    Route::post('/reservation/refund/{id}', [PaymentController::class, 'processReservationRefund']);

    Route::post('/transaction/setresult/{id}', [TransactionController::class, 'setResult']);
    Route::get('/transaction/getresult/{id}', [TransactionController::class, 'getResult']);
});

//question and answer
Route::post('/question_and_answer/store', [QuestionAnswerController::class, 'store']);
Route::post('/question_and_answer/edit/{id}', [QuestionAnswerController::class, 'edit']);
Route::post('/question_and_answer/delete/{id}', [QuestionAnswerController::class, 'delete']);
Route::get('/question_and_answer', [QuestionAnswerController::class, 'index']);


//favorite
Route::controller(FavoriteController::class)->middleware('jwt.verify')->group(function () {
    Route::post('/favorite/update', 'update');
    Route::post('/favorite/remove', 'remove');
    Route::post('/favorite', 'show')->withoutMiddleware('jwt.verify');

});


//points
Route::get('/points/{userid}', [PointController::class, 'points']);


//application rating
Route::controller(ApplicationRatingController::class)->middleware('jwt.verify')->group(function () {
    Route::post('/applicationrating/store', 'store');
    Route::post('/applicationrating/edit', 'edit');
    Route::get('/applicationrating/user/{user_id}', 'userapplicationrating')->withoutMiddleware('jwt.verify');
});

//offers
Route::get('/offers', [OfferController::class, 'index']);

