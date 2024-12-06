# ***App Workplace***

## App
#### :::src.workplace.apps.WorkplaceConfig

## Admin

### Workplace
#### :::src.workplace.admin.WorkplaceAdmin

### Room
#### :::src.workplace.admin.RoomAdmin

## Urls

### Home

1. ```/```

### Workplace

 1. ```workplace/```
 2. ```workplace/search/```
 3. ```workplace/(?P<pk>[-\w]+)$```
 4. ```workplace/create/$```
 5. ```workplace/(?P<pk>[-\w]+)/update$```
 6. ```workplace/(?P<pk>[-\w]+)/delete$```

### Room

 1. ```room/```
 2. ```room/search/```
 3. ```room/(?P<pk>[-\w]+)$```
 4. ```room/create/$```
 5. ```room/(?P<pk>[-\w]+)/update$```
 6. ```room/(?P<pk>[-\w]+)/delete$```

### REST API

1. ```api/v1/room/```
2. ```api/v1/workplace/```
