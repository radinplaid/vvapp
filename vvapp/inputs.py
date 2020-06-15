# AUTOGENERATED! DO NOT EDIT! File to edit: 00_inputs.ipynb (unless otherwise specified).

__all__ = ['checkbox', 'text', 'password', 'time', 'date', 'number', 'range_slider', 'slider', 'radio_buttons',
           'select', 'select_or_create']

# Cell
import ipyvuetify
from nbdev.imports import *

# Cell

def checkbox(v_model=False,
                  label=None,
                  hint=None,
                  persistent_hint=False,
                  class_=None,
                  style_=None,
                  **kwargs):
    """
    Checkbox input

    Function to generate an ipyvuetify Checkbox input widget.

    The value of the widget can be accessed or modified by the `v_model` property of the return value.

    See the vuetify documention for other arguments that can be passed as keyword arguments: https://vuetifyjs.com/en/components/selection-controls/

    Parameters:
    v_model : bool (optional, default None)
        Value of the time input, must be an element of choices

    label : str (optional, default False)
        Default value of the checkbox input

    hint : str (optional, default None)
        Hint text

    persistent_hint : bool (optional, default False)
        Set to True to display the hint when widget is not focused

    class_ : str (optional, default None)
        ipyvuetify HTML class string

    style_ : str (optional, default None)
        ipyvuetify HTML CSS string

    **kwargs
        Other arguments supported by ipyvuetify.TextField

    Returns:
    ipyvuetify.TextInput
        An ipyvuetify time input widget
    """
    ret = ipyvuetify.Checkbox(
        class_=class_,
        style_=style_,
        v_model=v_model,
        label=label,
        hint=hint,
        persistent_hint=persistent_hint)

    # Set other keyword arguments
    for arg in kwargs:
        setattr(ret, arg, kwargs[arg])

    # Return widget
    return ret


# Cell

def text(v_model=None,
             label=None,
             hint=None,
             persistent_hint=False,
             class_=None,
             style_=None,
             **kwargs):
    """
    Text input field

    Function to generate an ipyvuetify TextField input widget

    The value of the widget can be accessed or modified by the `v_model` property of the return value.

    See the vuetify documention for other arguments that can be passed as keyword arguments: https://vuetifyjs.com/en/components/text-fields/#api

    Parameters:

    v_model : str (optional, default None)
        Value of the input

    label : str (optional, default None)
        Description of the input

    hint : str or callable (optional, default None)
        Hint text or function generating int based on input value for validating input

    persistent_hint : bool (optional, default False)
        Set to True to display the hint when widget is not focused

    class_ : str (optional, default None)
        ipyvuetify HTML class string

    style_ : str (optional, default None)
        ipyvuetify HTML CSS string

    **kwargs
        Other arguments supported by ipyvuetify.TextField

    Returns:

    ipyvuetify.TextInput
        An ipyvuetify password input widget
    """

    # Set values for arguments
    if not callable(hint):
        hint_text = hint
    else:
        hint_text = ''

    ret = ipyvuetify.TextField(
        label=label,
        v_model=v_model,
        hint=hint_text,
        persistent_hint=persistent_hint,
        class_=class_,
        style_=style_
    )

    # Set other keyword arguments
    for arg in kwargs:
        setattr(ret, arg, kwargs[arg])

    # Apply validation, if function provided
    if callable(hint):
        error_hint = hint(ret.v_model)
        if error_hint is None:
            ret.hint = ''
            ret.error = False
        else:
            ret.hint = error_hint
            ret.error = True

        # When the value of the widget changes, validation will take place
        def on_value_change(change):
            error_hint = hint(ret.v_model)
            if error_hint is None:
                ret.hint = ''
                ret.error = False
            else:
                ret.hint = error_hint
                ret.error = True

        ret.observe(on_value_change, names='v_model')

    # Return widget
    return ret

# Cell

def password(v_model=None,
             label=None,
             hint=None,
             persistent_hint=False,
             class_=None,
             style_=None,
             **kwargs):
    """
    Password input field

    Function to generate an ipyvuetify TextField input widget with 'password' type prop.

    The value of the widget can be accessed or modified by the `v_model` property of the return value.

    See the vuetify documention for other arguments that can be passed as keyword arguments: https://vuetifyjs.com/en/components/text-fields/#api

    Parameters:

    v_model : str (optional, default None)
        Value of the input

    label : str (optional, default None)
        Description of the input

    hint : str or callable (optional, default None)
        Hint text or function generating int based on input value for validating input

    persistent_hint : bool (optional, default False)
        Set to True to display the hint when widget is not focused

    class_ : str (optional, default None)
        ipyvuetify HTML class string

    style_ : str (optional, default None)
        ipyvuetify HTML CSS string

    **kwargs
        Other arguments supported by ipyvuetify.TextField

    Returns:

    ipyvuetify.TextInput
        An ipyvuetify password input widget
    """
    ret = ipyvuetify.TextField()

    # Set values for arguments
    ret.label = label
    if not callable(hint):
        ret.hint = hint
    ret.persistent_hint = persistent_hint
    ret.v_model = v_model
    ret.class_ = class_
    ret.style_ = style_

    # Set other keyword arguments
    for arg in kwargs:
        setattr(ret, arg, kwargs[arg])

    ret.type = 'password'

    # Apply validation, if function provided
    if callable(hint):
        error_hint = hint(ret.v_model)
        if error_hint is None:
            ret.hint = ''
            ret.error = False
        else:
            ret.hint = error_hint
            ret.error = True

        # When the value of the widget changes, validation will take place
        def on_value_change(change):
            error_hint = hint(ret.v_model)
            if error_hint is None:
                ret.hint = ''
                ret.error = False
            else:
                ret.hint = error_hint
                ret.error = True

        ret.observe(on_value_change, names='v_model')

    # Return widget
    return ret

# Cell

def time(v_model=None,
         label=None,
         hint=None,
         persistent_hint=False,
         class_=None,
         style_=None,
         **kwargs):
    """
    Time input field

    Function to generate an ipyvuetify TextField input widget with 'time' type prop.

    The value of the widget can be accessed or modified by the `v_model` property of the return value.

    See the vuetify documention for other arguments that can be passed as keyword arguments: https://vuetifyjs.com/en/components/text-fields/#api

    Parameters:
    v_model : str (optional, default None)
        Value of the time input, format: HH:MM

    label : str (optional, default None)
        Description of the input

    hint : str or callable (optional, default None)
        Hint text or function generating int based on input value for validating input

    persistent_hint : bool (optional, default False)
        Set to True to display the hint when widget is not focused

    class_ : str (optional, default None)
        ipyvuetify HTML class string

    style_ : str (optional, default None)
        ipyvuetify HTML CSS string

    **kwargs
        Other arguments supported by ipyvuetify.TextField

    Returns:
    ipyvuetify.TextInput
        An ipyvuetify time input widget
    """
    ret = ipyvuetify.TextField()

    # Set values for arguments
    ret.label = label
    if not callable(hint):
        ret.hint = hint
    ret.persistent_hint = persistent_hint
    ret.v_model = v_model
    ret.class_ = class_
    ret.style_ = style_

    # Set other keyword arguments
    for arg in kwargs:
        setattr(ret, arg, kwargs[arg])

    ret.type = 'time'

    # Apply validation, if function provided
    if callable(hint):
        error_hint = hint(ret.v_model)
        if error_hint is None:
            ret.hint = ''
            ret.error = False
        else:
            ret.hint = error_hint
            ret.error = True

        # When the value of the widget changes, validation will take place
        def on_value_change(change):
            error_hint = hint(ret.v_model)
            if error_hint is None:
                ret.hint = ''
                ret.error = False
            else:
                ret.hint = error_hint
                ret.error = True

        ret.observe(on_value_change, names='v_model')

    # Return widget
    return ret

# Cell

def date(v_model=None,
         label=None,
         hint=None,
         persistent_hint=False,
         class_=None,
         style_=None,
         **kwargs):
    """
    Date input field

    Function to generate an ipyvuetify TextField input widget with 'date' type prop.

    The value of the widget can be accessed or modified by the `v_model` property of the return value.

    See the vuetify documention for other arguments that can be passed as keyword arguments: https://vuetifyjs.com/en/components/text-fields/#api

    Parameters:

    v_model : str (optional, default None)
        Value of the date input, format: YYYY-mm-dd

    label : str (optional, default None)
        Description of the input

    hint : str or callable (optional, default None)
        Hint text or function generating int based on input value for validating input

    persistent_hint : bool (optional, default False)
        Set to True to display the hint when widget is not focused

    class_ : str (optional, default None)
        ipyvuetify HTML class string

    style_ : str (optional, default None)
        ipyvuetify HTML CSS string

    **kwargs
        Other arguments supported by ipyvuetify.TextField

    Returns:

    ipyvuetify.TextInput
        An ipyvuetify time input widget
    """
    ret = ipyvuetify.TextField()

    # Set values for arguments
    ret.label = label
    if not callable(hint):
        ret.hint = hint
    ret.persistent_hint = persistent_hint
    ret.v_model = v_model
    ret.class_ = class_
    ret.style_ = style_

    # Set other keyword arguments
    for arg in kwargs:
        setattr(ret, arg, kwargs[arg])

    ret.type = 'date'

    # Apply validation, if function provided
    if callable(hint):
        error_hint = hint(ret.v_model)
        if error_hint is None:
            ret.hint = ''
            ret.error = False
        else:
            ret.hint = error_hint
            ret.error = True

        # When the value of the widget changes, validation will take place
        def on_value_change(change):
            error_hint = hint(ret.v_model)
            if error_hint is None:
                ret.hint = ''
                ret.error = False
            else:
                ret.hint = error_hint
                ret.error = True

        ret.observe(on_value_change, names='v_model')

    # Return widget
    return ret

# Cell

def number(v_model=None,
           min_value=None,
           max_value=None,
           label=None,
           hint=None,
           persistent_hint=False,
           class_=None,
           style_=None,
           validation_function=None,
           **kwargs):
    """
    Number input field

    Function to generate an ipyvuetify TextField input widget with 'numer' type prop.

    The value of the widget can be accessed or modified by the `v_model` property of the return value.

    See the vuetify documention for other arguments that can be passed as keyword arguments: https://vuetifyjs.com/en/components/text-fields/#api

    Parameters:

    v_model : str (optional, default None)
        Value of the number input

    min_value : float (optional)
        Minimum value for the widget for validation warning

    max-value : float (optional)
        Maximum value for the widget for validation warning

    label : str (optional, default None)
        Description of the input

    hint : str or callable (optional, default None)
        Hint text or function generating int based on input value for validating input

    persistent_hint : bool (optional, default False)
        Set to True to display the hint when widget is not focused

    class_ : str (optional, default None)
        ipyvuetify HTML class string

    style_ : str (optional, default None)
        ipyvuetify HTML CSS string

    validation_function : callable (optional)
        Validation function to call to validate input, overrides default validation

    **kwargs
        Other arguments supported by ipyvuetify.TextField

    Returns:

    ipyvuetify.TextInput
        An ipyvuetify number input widget with optional min/max value validation
    """
    ret = ipyvuetify.TextField()

    # Set values for arguments
    ret.label = label
    if not callable(hint):
        ret.hint = hint
    ret.persistent_hint = persistent_hint
    ret.v_model = v_model
    ret.class_ = class_
    ret.style_ = style_

    # Set other keyword arguments
    for arg in kwargs:
        setattr(ret, arg, kwargs[arg])

    ret.type = 'number'

    def _validate_numeric_input(widget=ret,
                                min_value=min_value,
                                max_value=max_value):
        """
        When `value` changes, try to change the format of `value` to
        numeric and if that fails, mark the input as invalid and display a helpful message
        """

        try:
            widget.v_model = float(widget.v_model)
            widget.error = False
            widget.persistent_hint = False
            widget.hint = ""

            if min_value is not None and float(widget.v_model) < min_value:
                widget.error = True
                widget.persistent_hint = True
                widget.hint = (
                    "Input: {value} is less than the minimum supported value {min_value}. "
                    .format(value=widget.v_model, min_value=min_value))

            if max_value is not None and float(widget.v_model) > max_value:
                widget.error = True
                widget.persistent_hint = True
                widget.hint = ("Input: {value} is greater than the maximum "
                               "supported value {max_value}.".format(
                                   value=widget.v_model, max_value=max_value))

        except:
            widget.error = True
            widget.persistent_hint = True

            if max_value is not None and min_value is not None:
                widget.hint = "Enter an number in range [{min_value}, {max_value}]".format(
                    min_value=min_value, max_value=max_value)
            elif min_value is not None:
                widget.hint = "Enter an number in range [{min_value}, ]".format(
                    min_value=min_value)
            elif max_value is not None:
                widget.hint = "Enter an number in range [, {max_value}]".format(
                    max_value=max_value)
            else:
                widget.error = False
                widget.hint = None

        try:
            if int(widget.v_model) == widget.v_model:
                widget.v_model = int(widget.v_model)
            else:
                pass
        except:
            pass

    # Apply validation, if function provided
    if callable(validation_function):
        def on_value_change(change):
            validation_function(ret)

        ret.observe(on_value_change, names='v_model')
        validation_function(ret)
    # Otherwise, use default validation
    else:
        def on_value_change(change):
            _validate_numeric_input(ret)

        ret.observe(on_value_change, names="v_model")
        _validate_numeric_input(ret)

    # Return widget
    return ret

# Cell


def range_slider(min=None,
           max=None,
           vertical=False,
           v_model=None,
           label=None,
           hint=None,
           persistent_hint=False,
           class_='mx-6 mt-8',
           style_=None,
           thumb_size=24,
           tick_size=4,
           ticks=True,
           step=None,
           thumb_label='always',
           **kwargs):
    """
    Range Slider input

    Function to generate an ipyvuetify Range Slider input widget.

    The value of the widget can be accessed or modified by the `v_model` property of the return value.

    See the vuetify documention for other arguments that can be passed as keyword arguments: https://vuetifyjs.com/en/components/sliders/

    Parameters:
    min : float
        Minimum value of slider

    max : float
        Maximum value of slider

    step : float (optional)
        Step size for slider, default: (max-min)/10

    v_model : list (optional)
        Default value of range slider (defaults to [min,max]))

    label : str (optional, default None)
        Description of the input

    hint : str or callable (optional, default None)
        Hint text or function generating int based on input value for validating input

    persistent_hint : bool (optional, default False)
        Set to True to display the hint when widget is not focused

    class_ : str (optional, default None)
        ipyvuetify HTML class string

    style_ : str (optional, default None)
        ipyvuetify HTML CSS string

    thumb_size : int (optional, default 24)
        Size of thumb widget in pixels

    tick_size : int (optional, default 4)
        Size of slider ticks in pixels

    ticks : bool (default True)
        Whether to display slider ticks

    thumb_label : bool/str (optional, default 'always')
        How to display thumb label

    **kwargs
        Other arguments supported by ipyvuetify.TextField

    Returns:
    ipyvuetify.Slider
        An ipyvuetify slider
    """
    if min is None:
        min = 0
    if max is None:
        max = 1

    # If no default is provided, default to [min,max]
    if v_model is None:
        v_model=[min,max]

    # If no step, divide interval by 10
    if step is None:
        step = (max - min) / 10.0


    ret = ipyvuetify.RangeSlider(min=min,
                            max=max,
                            thumb_size=thumb_size,
                            tick_size=tick_size,
                            ticks=ticks,
                            step=step,
                            thumb_label=thumb_label,
                            vertical=vertical,
                            class_=class_,
                            v_model=v_model,
                            label=label,
                            hint=hint,
                            persistent_hint=persistent_hint,
                            children=[])

    # Set other keyword arguments
    for arg in kwargs:
        setattr(ret, arg, kwargs[arg])

    # Return widget
    return ret

# Cell


def slider(min=None,
           max=None,
           vertical=False,
           v_model=None,
           label=None,
           hint=None,
           persistent_hint=False,
           class_='mx-6 mt-8',
           style_=None,
           thumb_size=24,
           tick_size=4,
           ticks=True,
           step=None,
           thumb_label='always',
           **kwargs):
    """
    Slider input

    Function to generate an ipyvuetify slider input widget.

    The value of the widget can be accessed or modified by the `v_model` property of the return value.

    See the vuetify documention for other arguments that can be passed as keyword arguments: https://vuetifyjs.com/en/components/sliders/

    Parameters:
    min : float
        Minimum value of slider

    max : float
        Maximum value of slider

    step : float (optional)
        Step size for slider, default: (max-min)/10

    v_model : float (optional)
        Default value of slider (defaults to min)

    label : str (optional, default None)
        Description of the input

    hint : str or callable (optional, default None)
        Hint text or function generating int based on input value for validating input

    persistent_hint : bool (optional, default False)
        Set to True to display the hint when widget is not focused

    class_ : str (optional, default None)
        ipyvuetify HTML class string

    style_ : str (optional, default None)
        ipyvuetify HTML CSS string

    thumb_size : int (optional, default 24)
        Size of thumb widget in pixels

    tick_size : int (optional, default 4)
        Size of slider ticks in pixels

    ticks : bool (default True)
        Whether to display slider ticks

    thumb_label : bool/str (optional, default 'always')
        How to display thumb label

    **kwargs
        Other arguments supported by ipyvuetify.TextField

    Returns:
    ipyvuetify.Slider
        An ipyvuetify slider
    """
    if min is None:
        min = 0
    if max is None:
        max = 1

    ret = ipyvuetify.Slider(min=min,
                            max=max,
                            thumb_size=thumb_size,
                            tick_size=tick_size,
                            ticks=ticks,
                            step=step,
                            thumb_label=thumb_label,
                            vertical=vertical,
                            class_=class_,
                            v_model=v_model,
                            label=label,
                            hint=hint,
                            persistent_hint=persistent_hint,
                            children=[])

    # Set other keyword arguments
    for arg in kwargs:
        setattr(ret, arg, kwargs[arg])

    # If no default is given, set it to the first
    if v_model is None:
        ret.v_model = min

    # If no step, divide interval by 10
    if step is None:
        ret.step = (max - min) / 10.0

    # Return widget
    return ret

# Cell

def radio_buttons(choices,
                  row=False,
                  v_model=None,
                  label=None,
                  hint=None,
                  persistent_hint=False,
                  class_='px-2 my-0 py-2',
                  style_=None,
                  **kwargs):
    """
    Radio Button input field

    Function to generate an ipyvuetify Radio Buttons input widget.

    The value of the widget can be accessed or modified by the `v_model` property of the return value.

    See the vuetify documention for other arguments that can be passed as keyword arguments: https://vuetifyjs.com/en/components/selection-controls/

    Parameters:
    choices : list or dict
        Choices to appear in radio button

    v_model : str (optional, default None)
        Value of the time input, must be an element of choices

    row : bool
        If True choices will be displayed in a row, otherwise in a column

    label : str (optional, default None)
        Description of the input

    hint : str or callable (optional, default None)
        Hint text or function generating int based on input value for validating input

    persistent_hint : bool (optional, default False)
        Set to True to display the hint when widget is not focused

    class_ : str (optional, default None)
        ipyvuetify HTML class string

    style_ : str (optional, default None)
        ipyvuetify HTML CSS string

    **kwargs
        Other arguments supported by ipyvuetify.TextField

    Returns:
    ipyvuetify.TextInput
        An ipyvuetify time input widget
    """
    ret = ipyvuetify.RadioGroup(
        class_=class_,
        style_=style_,
        v_model=v_model,
        label=label,
        hint=hint,
        persistent_hint=persistent_hint,
        row=row,
        children=[])

    # Set other keyword arguments
    for arg in kwargs:
        setattr(ret, arg, kwargs[arg])

    if isinstance(choices,list):
        ret.children = [ipyvuetify.Radio(label=i, value=i) for i in choices]
    elif isinstance(choices,dict):
        ret.children = [ipyvuetify.Radio(label=i, value=choices[i]) for i in choices]
    else:
        raise Exception("choices must be a dict or a list")

    # If no default is given, set it to the first
    if v_model is None:
        ret.v_model = choices[0]

    # Return widget
    return ret


# Cell

def select(items,
           v_model=None,
           multiple=False,
                  label=None,
                  hint=None,
                  persistent_hint=False,
                  class_=None,
                  style_=None,
                  small_chips=False,
                  deletable_chips=False,
                  **kwargs):
    """
    Select / Dropdown input

    Function to generate an ipyvuetify Dropdown input widget.

    The value of the widget can be accessed or modified by the `v_model` property of the return value.

    See the vuetify documention for other arguments that can be passed as keyword arguments: https://vuetifyjs.com/en/components/selects/

    Parameters:
    items : list
        Items to choose from in dropdown

    v_model : bool (optional, default None)
        Value of the time input, must be an element of choices

    multiple : bool
        Whether to allow multiple selected values

    label : str (optional, default False)
        Default value of the checkbox input

    hint : str (optional, default None)
        Hint text

    persistent_hint : bool (optional, default False)
        Set to True to display the hint when widget is not focused

    class_ : str (optional, default None)
        ipyvuetify HTML class string

    style_ : str (optional, default None)
        ipyvuetify HTML CSS string

    small_chips : bool (optional, default False)
        display selection as small chips

    deletable_chips : bool (optional, default False)
        display x on selection(s) to remove

    **kwargs
        Other arguments supported by ipyvuetify.TextField

    Returns:
    ipyvuetify.TextInput
        An ipyvuetify time input widget
    """

    if isinstance(items,dict):
        items = [{'text':i,'value':items[i]} for i in items]

    if multiple and not isinstance(v_model,list):
        v_model=[v_model]

    ret = ipyvuetify.Select(
        items=items,
        multiple=multiple,
        class_=class_,
        style_=style_,
        v_model=v_model,
        label=label,
        hint=hint,
        small_chips=small_chips,
        deletable_chips=deletable_chips,
        persistent_hint=persistent_hint)

    # Set other keyword arguments
    for arg in kwargs:
        setattr(ret, arg, kwargs[arg])

    # Return widget
    return ret


# Cell


def select_or_create(items,
                     v_model=None,
                     multiple=False,
                     label=None,
                     hint='Select or create item(s)',
                     persistent_hint=True,
                     class_=None,
                     style_=None,
                     small_chips=True,
                     deletable_chips=True,
                     hide_selected=True,
                     **kwargs):
    """
    Select / Dropdown input

    Function to generate an ipyvuetify Combobox input widget.

    The value of the widget can be accessed or modified by the `v_model` property of the return value.

    See the vuetify documention for other arguments that can be passed as keyword arguments: https://vuetifyjs.com/en/components/combobox/

    Parameters:
    items : list
        Items to choose from in dropdown

    v_model : bool (optional, default None)
        Value of the time input, must be an element of choices

    multiple : bool
        Whether to allow multiple selected values

    hint : str
        Help text to display

    persistent_hint : bool
        Whether to always show hint text

    label : str (optional, default False)
        Default value of the checkbox input

    class_ : str (optional, default None)
        ipyvuetify HTML class string

    style_ : str (optional, default None)
        ipyvuetify HTML CSS string

    small_chips : bool (optional, default True)
        display selection as small chips

    deletable_chips : bool (optional, default True)
        display x on selection(s) to remove

    hide_selected : bool (default True)
        Hide selected elements from menu

    **kwargs
        Other arguments supported by ipyvuetify.TextField

    Returns:
    ipyvuetify.TextInput
        An ipyvuetify time input widget
    """

    if isinstance(items, dict):
        items = [{'text': i, 'value': items[i]} for i in items]

    if multiple and v_model is not None and not isinstance(v_model, list):
        v_model = [v_model]

    ret = ipyvuetify.Combobox(
        items=items,
        multiple=multiple,
        class_=class_,
        style_=style_,
        v_model=v_model,
        label=label,
        small_chips=small_chips,
        deletable_chips=deletable_chips,
        hide_selected=hide_selected,
        persistent_hint=persistent_hint,
        hint=hint,
        v_slots=[{
            'name':
            'no-data',
            'children':
            ipyvuetify.ListItem(children=[
                ipyvuetify.ListItemContent(children=[
                    ipyvuetify.ListItemTitle(children=[
                        'Your search returned no items. Press Enter to create a new one'
                    ])
                ])
            ])
        }])

    # Set other keyword arguments
    for arg in kwargs:
        setattr(ret, arg, kwargs[arg])

    # Return widget
    return ret