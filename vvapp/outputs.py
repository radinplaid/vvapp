# AUTOGENERATED! DO NOT EDIT! File to edit: 01_outputs.ipynb (unless otherwise specified).

__all__ = ['PandasTable', 'markdown', 'info_snackbar']

# Cell
import ipyvuetify
from nbdev.imports import *

# Cell

import pandas as pd
import traitlets
import ipyvuetify as v
import json

class PandasTable(v.VuetifyTemplate):
    """
    Vuetify DataTable rendering of a pandas DataFrame

    Args:
        data (pandas.DataFrame) - the data to render
        title (str) - optional title

    Modified from Source: https://jupyter-tutorial.readthedocs.io/de/latest/workspace/jupyter/ipywidgets/libs/ipyvuetify.html
    """

    headers = traitlets.List([]).tag(sync=True, allow_null=True)
    items = traitlets.List([]).tag(sync=True, allow_null=True)
    search = traitlets.Unicode('').tag(sync=True)
    title = traitlets.Unicode('DataFrame').tag(sync=True)
    index_col = traitlets.Unicode('').tag(sync=True)
    template = traitlets.Unicode('''
        <template>
          <v-card>
            <v-card-title>
              <span class="title font-weight-bold">{{ title }}</span>
              <v-spacer></v-spacer>
                <v-text-field
                    v-model="search"
                    append-icon="search"
                    label="Search ..."
                    single-line
                    hide-details
                ></v-text-field>
            </v-card-title>
            <v-data-table
                :headers="headers"
                :items="items"
                :search="search"
                :item-key="index_col"
                :rows-per-page-items="[25, 50, 250, 500]"
            >
                <template v-slot:no-data>
                  <v-alert :value="true" color="error" icon="warning">
                    Sorry, nothing to display here :(
                  </v-alert>
                </template>
                <template v-slot:no-results>
                    <v-alert :value="true" color="warning" icon="warning">
                      Your search for "{{ search }}" found no results.
                    </v-alert>
                </template>
                <template v-slot:items="rows">
                  <td v-for="(element, label, index) in rows.item"
                      @click=cell_click(element)
                      >
                    {{ element }}
                  </td>
                </template>
            </v-data-table>
          </v-card>
        </template>
        ''').tag(sync=True)

    def __init__(self, *args,
                 data=pd.DataFrame(),
                 title=None,
                 **kwargs):
        super().__init__(*args, **kwargs)
        data = data.reset_index()
        self.index_col = data.columns[0]
        headers = [{
              "text": col,
              "value": col
            } for col in data.columns]
        headers[0].update({'align': 'left', 'sortable': True})
        self.headers = headers
        self.items = json.loads(
            data.to_json(orient='records'))
        if title is not None:
            self.title = title


# Cell

from markdown import markdown as md
import ipywidgets
def markdown(*args, **kwargs):
    """
    Render input string(s) as markdown

    Parameters
    *args : str or list of strings
        String(s) to render as markdown
    **kwargs : any
        arguments supported by the markdown class

    """
    return ipywidgets.HTML(
        md(
            '\n'.join(args),
            **kwargs
        )
    )

# Cell

class _InfoSnackbar(v.VuetifyTemplate):
    color = traitlets.Unicode("primary").tag(sync=True, allow_null=True)
    message = traitlets.Unicode("").tag(sync=True, allow_null=False)
    timeout = traitlets.Integer(5000).tag(sync=True, allow_null=True)
    active = traitlets.Bool(True).tag(sync=True, allow_null=True)
    multi_line = traitlets.Bool(True).tag(sync=True, allow_null=True)

    template = traitlets.Unicode(
        """
        <template>
          <div class="text-center">
            <v-snackbar
                v-model="active"
                :color="color"
                :multi-line="multi_line"
                :timeout="timeout"
            >
              {{message}}

            <v-btn
              color="white"
              text
              @click="active = false"
            >
              Close
            </v-btn>

            </v-snackbar>
          </div>
          </template>

        """
    ).tag(sync=True)

    def __init__(
        self,
        snackbar=False,
        message=None,
        multi_line=True,
        color="primary",
        timeout=6000,
        active=True,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.color = color
        self.timeout = timeout
        self.active = active
        self.message = message
        self.multi_line = multi_line

def info_snackbar(snackbar=False,
        message=None,
        multi_line=True,
        color="primary",
        timeout=6000,
        active=True):
    """
    snackbar widget

    Useful for displaying information/messages

    message : str
        Status message to display
    timeout : int, optional default 6000
        How long to display the message (in milliseconds)
    multi_line : bool, optional default True
        Whether the snackbar should be multi-line (or not)
    color : str, optional default 'primary'
        ipyvuetify color of snackbar
        Typical options include ['primary','error','warning','success']
    active : bool, optional, default True
        Whether to display snackbar
        """
    return _InfoSnackbar(snackbar=snackbar,
                        message=message,
                        multi_line=multi_line,
                        color=color,
                        timeout=timeout,
                        active=active)