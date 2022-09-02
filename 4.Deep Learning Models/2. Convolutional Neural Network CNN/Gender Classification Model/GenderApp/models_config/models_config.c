model_config_list {
  config {
    name: 'gender_model'
	# Note that this is the model target path
    base_path: '/models/gender_model'
    model_platform: 'tensorflow'
	model_version_policy {
	  specific {
		versions: 1
	  }
	}
	version_labels {
	  key: 'production'
	  value: 1
	}
  }
}
