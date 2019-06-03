"""ProTwo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appTwo import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='Index'),
]




 mDb = AppDatabase.getDatabaseInstance(getApplicationContext());

        AppExecutors.getInstance().diskIO().execute(new Runnable() {
            @Override
            public void run() {
                LiveData<Favorite> favorite = mDb.favoriteDao().getFavoriteById(Integer.parseInt(movie.getId()));
                setFavorite(favorite.getValue());
            }
        });




    private void setFavorite(Boolean fav){
        if (fav) {
            isFav = true;
             ivStar.setImageResource(R.drawable.ic_star_yellow_48dp);
        } else {
            isFav = false;
             ivStar.setImageResource(R.drawable.ic_star_border_yellow_48dp);
        }
    }



     AppExecutors.getInstance().diskIO().execute(new Runnable() {
                    @Override
                    public void run() {
                        if (isFav) {
                            // delete item
                            viewModel.removeFavorite();
                        } else {
                            // insert item
                            viewModel.addFavorite();
                        }
                        runOnUiThread(new Runnable() {
                            @Override
                            public void run() {
                                setFavorite(!isFav);
                            }
                        });
                    }

                });
