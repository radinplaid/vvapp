# AUTOGENERATED! DO NOT EDIT! File to edit: 00_inputs.ipynb (unless otherwise specified).

__all__ = ['password', 'time', 'date']

# Cell

import ipyvuetify


def password(v_model=None,
             label=None,
             hint=None,
             persistent_hint=False,
             class_=None,
             style_=None,
             validation_function=None,
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
    validation_function : callable

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
         validation_function=None,
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
    validation_function : callable

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
         validation_function=None,
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
    validation_function : callable

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