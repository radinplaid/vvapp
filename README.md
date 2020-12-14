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
        

```python
from vvapp.inputs import __all__ as available_input_widgets
available_input_widgets
```




    ['switch',
     'checkbox',
     'text',
     'password',
     'time_input',
     'date',
     'date_range',
     'number',
     'range_slider',
     'slider',
     'radio_buttons',
     'select',
     'select_or_create',
     'button',
     'color_picker']



### text

```python
from vvapp.inputs import text
text(label='Text Input',hint='Enter some text',v_model='some text')
```

<img alt="Text Input" caption="Text Input Example" src="images/input_text.png">

### select (dropdown)

For a select input, the `v_model` can be a list:

```python
from vvapp.inputs import select
select(items=['one','two','three'],v_model='two')
```

<img alt="Select Input" caption="Select Input" src="images/select1.png">

... or a dict where the keys are the labels to be displayed and the values and the values

```python
select(items={'One':'one','Two':'two','Three':'three'},v_model='two')
```

<img alt="Select Input" caption="Select Input With dict input" src="images/select2.png">

Also, it is possible for multiple items to be selected via the `multiple` prop:

```python
tmp = select(items={'One':'one','Two':'two','Three':'three'},v_model=['one','two'],multiple=True)
tmp
```

<img alt="Select Input" caption="Multiple Select Input" src="images/select3.png">

```python
tmp.v_model
```




    ['one', 'two']



### select_or_create (combobox)

```python
from vvapp.inputs import select_or_create
select_or_create(items=['one','two','three'],v_model=['one','two'],multiple=True)

```

<img alt="Combobox Input" caption="Combobox" src="images/select_or_create.png">

### switch

```python
from vvapp.inputs import switch
switch(label='Switch example',v_model=True)
```

<img alt="Switch Input" caption="Switch Input Example" src="images/switch.png">

### checkbox

```python
from vvapp.inputs import checkbox
checkbox(label='Checkbox example',v_model=True)
```

<img alt="Checkbox Input" caption="Checkbox" src="images/checkbox.png">

### slider

```python
from vvapp.inputs import slider
slider(label='Slider Example',
       min=0,
       max=10,
       step=1,
       color='red',
       track_color='red',
       v_model=5)
```

<img alt="Slider Input" caption="Slider" src="images/slider.png">

### range_slider

```python
from vvapp.inputs import range_slider
range_slider(min=0,max=100,v_model=[40,60])
```

<img alt="Range Slider input" caption="Range Slider Example" src="images/range_slider.png">

### radio_buttons

```python
from vvapp.inputs import radio_buttons
radio_buttons(choices={
                    'Apple': 'apple',
                    'Blueberry': 'blueberry',
                    'Pumpkin': 'pumpkin'
                },
              label='What is your favourite pie flavour?',
              v_model='blueberry')
```

<img alt="Radio Button Input" caption="Radio Button" src="images/radio_buttons.png">

### date

```python
from vvapp.inputs import date
date(label='Please enter a date (format: YYYY-mm-dd)',
     v_model='2020-04-15',
     style_='max-width:320px')
```

<img alt="Date Input" caption="Date Input" src="images/input_date.png">

### time

```python
from vvapp.inputs import time_input
time_input(label='Please enter a time (format: HH:MM)',
     v_model='13:34',
     style_='max-width:320px')
```


<img alt="Time Input" caption="Time Input" src="images/input_time.png">


### integer

```python
from vvapp.inputs import integer
integer(placeholder='Enter an integer',
     style_='max-width:320px')
```

`integer` inputs have a default validation function that changes the `error` state of the input to True and prints a sensible hint if the value is less than `min_value` or greater than `max_value` or if the input is not an integer (i.e. a floating point number)

```python
from vvapp.inputs import integer
integer(label='Integer Input',
       v_model=50.123,
       min_value=0,
       max_value=100,
     style_='max-width:320px')
```

### number

```python
from vvapp.inputs import number
number(placeholder='Enter a number',
     style_='max-width:320px')
```

<img alt="Number Input" caption="Number Input" src="images/input_number.png">


`number` inputs have a default validation function that changes the `error` state of the input to True and prints a sensible hint if the value is less than `min_value` or greater than `max_value`

```python
from vvapp.inputs import number
number(label='Number Input',
       v_model=123,
       min_value=0,
       max_value=100,
     style_='max-width:320px')
```


<img alt="Number Input With Validation" caption="Number Input With Validation" src="images/input_number_validation.png">


### password

```python
from vvapp.inputs import password
pw = password(label='Please enter a password',v_model='correcthorsebatterystapler')
pw
```

<img alt="Password Input" caption="Password Input" src="images/input_password.png">


The value of of a vvapp widget is set/accessed by the `v_model` attribute, just like in ipyvuetify

```python
pw.v_model
```




    'correcthorsebatterystapler'



Here we demonstrate the use of a function to validate the value of the input.

In this example the password must be at least 12 characters, less than 64 characters and include at least one number:

```python
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

<img alt="Password Input with Validation" caption="Password Input with Validation" src="images/input_password_validation.png">


### button

```python
from vvapp.inputs import button
```

```python
def print_test_on_click(*args):
    print('test')

button(label='I print `test` on click',
       size='large',
       color='teal',
       dark=True,
       on_click=print_test_on_click)

```

<img alt="Button Input Example" caption="Button Input Example" src="images/input_button1.png">

```python
button(icon='mdi-recycle',
       size='large',
       color='teal',
       dark=True,
       fab=True,
       class_='ma-4'
      )
```

<img alt="Button Input Example" caption="Fab Style With Icon Button Input Example" src="images/input_button2.png">

### date_range

```python
from vvapp.inputs import date_range
temp = date_range(dates=['2020-01-01','2020-02-01'])
temp
```

<img alt="Date Range Input Example" caption="Date Range Input Example" src="images/daterange.png">


```python
temp.dates
```




    ['2020-01-01', '2020-02-01']



### color_picker

```python
from vvapp.inputs import color_picker
temp=color_picker()
temp
```

<img alt="Color Picker Input Example" caption="Color Picker Input Example" src="images/color_picker.png">


```python
temp.v_model
```

## Outputs

### PandasTable

```python
import pandas as pd
from vvapp.outputs import PandasTable
df = pd.DataFrame({'a':[1,2,3],'b':[2,3,4]})
PandasTable(data=df,title='My DataFrame')
```

<img alt="Pandas Dataframe Output" caption="Pandas Dataframe Output" src="images/output_pandas_table2.png">


The pandas DataFrame output has a nice warning/error display if the search returns zero results or if are no rows in the PandasDataframe:

```python
import pandas as pd
from vvapp.outputs import PandasTable
df = pd.DataFrame({'a':[1,2,3],'b':[2,3,4]})
PandasTable(data=df,title='My DataFrame')
```

<img alt="Pandas Dataframe Output No Search Results" caption="Pandas Dataframe Output No Search Results" src="images/output_pandas_table_zeroresults.png">


```python
import pandas as pd
from vvapp.outputs import PandasTable
PandasTable(data=pd.DataFrame(),title='My DataFrame')
```

<img alt="Pandas Dataframe Output No Data" caption="Pandas Dataframe Output No Data" src="images/output_pandas_table_nodata.png">


### Markdown

```python
from vvapp.outputs import markdown 

markdown("""
# Markdown Title

## Markdown Subtitle

Some body text

* a list element
* another list element
""")
```

<img alt="Output Markdown" caption="Markdown output example" src="images/output_markdown.png">


### Snackbar

```python
from vvapp.outputs import info_snackbar
info_snackbar(message='Message text', color='teal',timeout=10000)
```

<img alt="Output Snackbar" caption="Snackbar output example" src="images/snackbar.png">


### Dialog Button

```python
from vvapp.outputs import dialog_button
dialog_button(label='My Button',icon=None)
```

<img alt="Dialog Button Example" caption="Dialog Button Example" src="images/dialog_button.png">


### Container

```python
from vvapp.inputs import button
from vvapp.outputs import container
container(children=[
    button(color='red', label='Red'),
    button(color='blue', label='Blue'),
    button(color='green', label='Green')
])
```

<img alt="Container Output Example" caption="Container Output Example" src="images/container.png">


### Row

```python
from vvapp.inputs import button
from vvapp.outputs import row
container(children=[
    row(children=[button(color='red', label='Red')]),
    row(children=[button(color='blue', label='Blue')]),
    row(children=[button(color='green', label='Green')])
])
```

<img alt="Row Output Example" caption="Row Output Example" src="images/row.png">


### Column

```python
from vvapp.inputs import button
from vvapp.outputs import column
row(children=[
    column(order=1, cols=4, children=[button(color='red', label='Red')]),
    column(order=0, cols=4, children=[button(color='blue', label='Blue')]),
    column(order=2, cols=4, children=[button(color='green', label='Green')])
])
```

<img alt="Column Example" caption="Column Example" src="images/column.png">
