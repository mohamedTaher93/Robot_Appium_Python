locators = {
    "home_locators":{
        "ignoreNotifications": ("id", "com.android.permissioncontroller:id/permission_deny_button"),
        "allowLocationWhileUseApp": ("id", "com.android.permissioncontroller:id/permission_allow_foreground_only_button"),
        "selectLocation": ("id", "com.hungerstation.android.web:id/address_description"),
        "searchLocationField": ("id", "com.hungerstation.android.web:id/search_bar"),
        "searchLocationInput": ("id", "com.hungerstation.android.web:id/places_autocomplete_search_bar"),
        "firstAddressOption": ("xpath", "(//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout)[1]"),
        "confirmLocation": ("id", "com.hungerstation.android.web:id/confirm_drop_off_button"),
        "saveContinue": ("xpath", "//android.widget.Button[@text = 'Save and Continue']"),
        "homeBottomIcon": ("id", "com.hungerstation.android.web:id/restaurants_item"),
        "searchForRestaurant": ("id", "com.hungerstation.android.web:id/input_csc"),
        "searchRestaurantContainer": ("id", "com.hungerstation.android.web:id/searchSwipeLayout"),
        "restaurantTitle": ("id", "com.hungerstation.android.web:id/header_title")
    }
}