LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

# name of the librairy
LOCAL_MODULE := ogg

LOCAL_LIBRARIES := etk

LOCAL_C_INCLUDES := $(LOCAL_PATH)/tremor/ \
                    $(LOCAL_PATH)/ogg/

LOCAL_EXPORT_C_INCLUDES := $(LOCAL_PATH)

LOCAL_CFLAGS := -DOGG_VERSION_TAG_NAME="\"1.0.2-$(BUILD_DIRECTORY_MODE)\""
                -DTREMOR_VERSION_TAG_NAME="\"1.0.2-$(BUILD_DIRECTORY_MODE)\""

# load the common sources file of the platform
include $(LOCAL_PATH)/file.mk

LOCAL_SRC_FILES := $(FILE_LIST)

include $(BUILD_STATIC_LIBRARY)
