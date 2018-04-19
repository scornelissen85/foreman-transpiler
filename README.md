# foreman-transpiler
Simple script which can be used as proxy for Foreman, to convert YAML ignition to JSON.

Start script with
```
python proxy.sh 8080
```

This will proxy all requests to http://127.0.0.1:8080 to the foreman URL configured in proxy.py. Also it is required to have [ct](https://github.com/coreos/container-linux-config-transpiler) installed.
