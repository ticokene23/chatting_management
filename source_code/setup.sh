#!/bin/bash

# APPS = ($(echo "$APP_LIST" | tr ',' '\n'))
# DIRS = ($(echo "$DIR_LIST" | tr ',' '\n'))

# if [ "${#APPS[@]}" -eq "${#DIRS[@]}" ]; then
# 	FOR i in "${!APPS[@]}"
# 	do 
# 		if [ -d "$DIRS[$i]" ] && [ -d "$APPS[$i]" ]; then
			
# 		  # Control will enter here if $DIRECTORY doesn't exist.
# 			cd $DIRS[$i] && django-admin startproject $APPS[$i]

# 	done 

# fi

django-admin startproject $APP