# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class IndexAdmin(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        return redirect('/admin/')
    # end def
# end class