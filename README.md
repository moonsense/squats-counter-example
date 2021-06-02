# Squats Counter Example

A simple demo to get acceleration data from a mobile device and identify how many squat repetitions we've made using moonsense recording.

## Getting started

1. generate a new virtual envrionment.

```shell
virtualenv -p python3 venv
source activate venv/bin/activate
pip install -r reqquirements.txt
```

2. Run our example script. It will iterate on all the seessions and display our identified squat repetitions. See the blog post for
   reference.

To get data, you'll want to sign up to [moonsense](https://www.moonsense.io/). You'll get an api token like `your_secret_token`

```shell
export MOONSENSE_SECRET_TOKEN=your_secret_token python scripts/squat_counter.py
```

If you prefer jupyter notebooks, you can run scripts/squat_counter.ipynb instead.

Contributions and github issues are welcome!




   
