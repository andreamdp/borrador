# -*- encoding: utf-8 -*-
from geraldo import Report, landscape
from reportlab.lib.pagesizes import A5
from reportlab.lib.units import cm
from geraldo import Report, landscape, ReportBand, ObjectValue, SystemField,\
        BAND_WIDTH, Label, ReportGroup,FIELD_ACTION_COUNT, FIELD_ACTION_SUM, BAND_WIDTH, Line

from reportlab.lib.enums import TA_RIGHT, TA_CENTER,TA_LEFT
from reportlab.lib.pagesizes import A5
from reportlab.lib.units import cm

class ReportGrupoInst(Report):
   
    title='a'
    class band_summary(ReportBand):
        height = 0.8*cm
        elements = [
            Label(text="Total general:", top=0.1*cm, left=0),
            ObjectValue(attribute_name='id', top=0.1*cm, left=2.5*cm,\
                action=FIELD_ACTION_COUNT, display_format='%s '),
        ]
        borders = {'all': True}
    page_size = landscape(A5)
    margin_left = 2*cm
    margin_top = 0.5*cm
    margin_right = 0.5*cm
    margin_bottom = 0.5*cm

    class band_detail(ReportBand):
        height = 0*cm
        elements=(  )
    class band_page_header(ReportBand):
        height = 1.3*cm
        elements = [
            SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
           
            SystemField(expression=u'Page %(page_number)d of %(page_count)d', top=0.1*cm,
                width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
            ]
    #    borders = {'bottom': True}

    class band_page_footer(ReportBand):
        height = 0.5*cm
        elements = [
            Label(text="Colmed IX°", top=0.1*cm, left=0, style={'alignment': TA_LEFT,'fontName': 'Helvetica', 'fontSize': 10}),
            SystemField(expression=u' %(now:%b %d %Y)s, %(now:%H:%M)s hs.', top=0.1*cm,
                width=BAND_WIDTH, style={'alignment': TA_RIGHT,'fontName': 'Helvetica', 'fontSize': 10})
            ]
     #   borders = {'top': True}

    groups = [
        ReportGroup(attribute_name = 'institucion',
            band_header = ReportBand(
                height = 0.7*cm,
                elements = [
                    ObjectValue(attribute_name='Institucion', left=1, top=0.1*cm, width=20*cm,
                        get_value=lambda instance: 'Institucion: ' + (instance.institucion.nombre),
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 12}),
                   
                   # ObjectValue(attribute_name='especialidad', action=FIELD_ACTION_COUNT,
                   #     display_format='%s ', left=15*cm, top=0.1*cm,style={'fontName': 'Helvetica-Bold', 'fontSize': 12})
                   
                    ],
             #   borders = {'bottom': True},
                ),
            band_footer=ReportBand(
                height=0.7*cm,
                elements=[
                    ObjectValue(attribute_name='id', action=FIELD_ACTION_COUNT,
                        display_format='Total por Institucion: %s' , left=15*cm, top=0.1*cm,style={'fontName': 'Helvetica-BoldOblique', 'fontSize': 10.5})
                ],
                borders={'top': True, 'left':True, 'right':True,'bottom':True},
            ),
                        
         ),
        ReportGroup(attribute_name = 'especialidad',
            band_header = ReportBand(
                height = 0.5*cm,
                elements = [
                    ObjectValue(attribute_name='Especialidad', left=15, top=0.1*cm, width=20*cm,
                        get_value=lambda instance: (instance.especialidad.nombre),
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 10}),
                    ObjectValue(attribute_name='id', action=FIELD_ACTION_COUNT, display_format='%s ', left=10*cm, top=0.1*cm,
                    style={'fontName': 'Helvetica-Bold', 'fontSize': 10})
			
                   
                    ],
                #borders = {'bottom': True},
                ),
            
                        
         ),
        ]
class ReportGrupoInst2012(ReportGrupoInst):
    title="RESIDENCIAS AÑO 2012 DISTRITO IX"

class ReportGrupoInst2013(ReportGrupoInst):
    title="RESIDENCIAS AÑO 2013 DISTRITO IX"

