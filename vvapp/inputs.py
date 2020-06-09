# AUTOGENERATED! DO NOT EDIT! File to edit: 00_inputs.ipynb (unless otherwise specified).

__all__ = ['password', 'time', 'date', 'number']

# Cell

import ipyvuetify


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

    Parameters
    ----------
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

    Returns
    -------
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

import ipyvuetify


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

    Parameters
    ----------
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

    Returns
    -------
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

import ipyvuetify


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

    Parameters
    ----------
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

    Returns
    -------
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

import ipyvuetify


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

    Parameters
    ----------
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

    Returns
    -------
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