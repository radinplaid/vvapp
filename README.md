# vvapp
> A python library simplifying ipyvuetify voila application building.


## Documentation

https://radinplaid.github.io/vvapp/

## Install

`pip install vvapp`

## Inputs

`vvapp` is meant to be used in Jupyter, so launching jupyter first (`$jupyter notebook`).

There are a few key things to keep in mind when getting up and running with `vvapp`:

* `v_model`
    * The value of `vvapp` inputs is set and accessed via the `v_model` attribute, following the `ipyvuetify` convention
* `class_`
    * This is where you put `vuetify.js` class properties, like `ma-4` to add margins around the input
* `style_`
    * This is where you can add CSS to your elements
* `hint`
    * The `hint` can be a string *or* a callable to provide input validation
    * If `hint` is a callable, it must return a string or None; if it returns a string, the input is marked as invalid and the string is displayed
        

```
from vvapp.inputs import __all__ as available_input_widgets
available_input_widgets
```




    ['password', 'time', 'date', 'number']



### date

```
from vvapp.inputs import date
date(label='Please enter a date (format: YYYY-mm-dd)',
     v_model='2020-04-15',
     style_='max-width:320px')
```

```
Image(filename="docs/img/input_date.png")
```




![png](docs/images/output_7_0.png)



### time

```
from vvapp.inputs import time
time(label='Please enter a time (format: HH:MM)',
     v_model='13:34',
     style_='max-width:320px')
```

```
Image(filename="docs/img/input_time.png")
```




![png](docs/images/output_10_0.png)



### number

```
from vvapp.inputs import number
number(placeholder='Enter a number',
     style_='max-width:320px')
```

```
Image(filename="docs/img/input_number.png")
```




![png](docs/images/output_13_0.png)



`number` inputs have a default validation function that changes the `error` state of the input to True and prints a sensible hint if the value is less than `min_value` or greater than `max_value`

```
from vvapp.inputs import number
number(label='Number Input',
       v_model=123,
       min_value=0,
       max_value=100,
     style_='max-width:320px')
```

```
Image(filename="docs/img/input_number_validation.png")
```




![png](docs/images/output_16_0.png)



### password

```
from vvapp.inputs import password
pw = password(label='Please enter a password',v_model='correcthorsebatterystapler')
pw
```

```
Image(filename="docs/img/input_password.png")
```




![png](docs/images/output_19_0.png)



The value of of a vvapp widget is set/accessed by the `v_model` attribute, just like in ipyvuetify

```
pw.v_model
```




    'correcthorsebatterystapler'



Here we demonstrate the use of a function to validate the value of the input.

In this example the password must be at least 12 characters, less than 64 characters and include at least one number:

```
import re
def validate_pw(widget_value):
    if widget_value is None:
        return 'Input must not be None'

    else:
        if len(widget_value) < 12:
            return 'Too Short!'

        if len(widget_value) > 64:
            return 'Too Long!'

        if not re.search('[0-9]+',widget_value):
            return 'Must contain at least one number!'

    return None

pw = password(label='Please enter a password',v_model='correcthorsebatterystapler', hint=validate_pw)
pw
```

```
Image(filename="docs/img/input_password_validation.png")
```




![png](docs/images/output_24_0.png)



# Outputs

```
import pandas as pd
from vvapp.outputs import PandasTable
df = pd.DataFrame({'a':[1,2,3],'b':[2,3,4]})
PandasTable(data=df,title='My DataFrame')
```

```
Image(filename="docs/img/output_pandas_table.png")
```




![png](docs/images/output_27_0.png)



The pandas DataFrame output has a nice warning/error display if the search returns zero results or if are no rows in the PandasDataframe:

```
import pandas as pd
from vvapp.outputs import PandasTable
df = pd.DataFrame({'a':[1,2,3],'b':[2,3,4]})
PandasTable(data=df,title='My DataFrame')
```

```
Image(filename="docs/img/output_pandas_table_zeroresults.png")
```




![png](docs/images/output_30_0.png)



```
import pandas as pd
from vvapp.outputs import PandasTable
PandasTable(data=pd.DataFrame(),title='My DataFrame')
```

```
Image(filename="docs/img/output_pandas_table_nodata.png")
```




![png](docs/images/output_32_0.png)


