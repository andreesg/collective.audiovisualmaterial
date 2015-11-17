#!/usr/bin/python
# -*- coding: utf-8 -*-

from zope import schema
from zope.interface import Interface
from collective.audiovisualmaterial import MessageFactory as _
from ..utils.vocabularies import _createPriorityVocabulary, _createInsuranceTypeVocabulary
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

priority_vocabulary = SimpleVocabulary(list(_createPriorityVocabulary()))
insurance_type_vocabulary = SimpleVocabulary(list(_createInsuranceTypeVocabulary()))

from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from collective.object.utils.widgets import SimpleRelatedItemsFieldWidget, AjaxSingleSelectFieldWidget
from collective.object.utils.source import ObjPathSourceBinder
from plone.directives import dexterity, form

class ListField(schema.List):
    """We need to have a unique class for the field list so that we
    can apply a custom adapter."""
    pass

# # # # # # # # # # # # #
# Widget interface      #
# # # # # # # # # # # # #

class IFormWidget(Interface):
    pass


# # # # # # # # # # # # # #
# DataGrid interfaces     # 
# # # # # # # # # # # # # #

# Title and author

class ITitle(Interface):
    title = schema.TextLine(title=_(u'Title'), required=True)

    
class IAuthor(Interface):
    #author = schema.TextLine(title=_(u'Author'), required=False)

    authors = RelationList(
        title=_(u'Author'),
        default=[],
        missing_value=[],
        value_type=RelationChoice(
            title=u"Related",
            source=ObjPathSourceBinder(portal_type='PersonOrInstitution')
        ),
        required=False
    )
    form.widget('authors', SimpleRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')

    #role = schema.TextLine(title=_(u'label_author_role'), required=False)
    roles = schema.List(
        title=_(u'label_author_role'),
        required=False,
        value_type=schema.TextLine(),
        missing_value=[],
        default=[]
    )
    form.widget('roles', AjaxSingleSelectFieldWidget, vocabulary="collective.bibliotheek.role")

class IIllustrator(Interface):
    #illustrator = schema.TextLine(title=_(u'Illustrator'), required=False)

    illustrators = RelationList(
        title=_(u'Illustrator'),
        default=[],
        missing_value=[],
        value_type=RelationChoice(
            title=u"Related",
            source=ObjPathSourceBinder(portal_type='PersonOrInstitution')
        ),
        required=False
    )
    form.widget('illustrators', SimpleRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')

    roles = schema.List(
        title=_(u'label_author_role'),
        required=False,
        value_type=schema.TextLine(),
        missing_value=[],
        default=[]
    )
    form.widget('roles', AjaxSingleSelectFieldWidget, vocabulary="collective.bibliotheek.role")
    
class ICorpAuthor(Interface):
    corpAuthor = RelationList(
        title=_(u'Corp.author', default=u'Corp.author'),
        default=[],
        value_type=RelationChoice(
            title=u"Related",
            source=ObjPathSourceBinder(portal_type='PersonOrInstitution')
        ),
        required=False
    )
    form.widget('corpAuthor', SimpleRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')

class IPlace(Interface):
    term =  schema.TextLine(title=_(u'Place'), required=False)

class IPublisher(Interface):
    publisher = RelationList(
        title=_(u'Publisher'),
        default=[],
        missing_value=[],
        value_type=RelationChoice(
            title=u"Related",
            source=ObjPathSourceBinder(portal_type='PersonOrInstitution')
        ),
        required=False
    )
    form.widget('publisher', SimpleRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')

class IPlacePrinted(Interface):
    term = schema.TextLine(title=_(u'Place printed'), required=False)

class IPrinter(Interface):
    printer = RelationList(
        title=_(u'Printer'),
        default=[],
        missing_value=[],
        value_type=RelationChoice(
            title=u"Related",
            source=ObjPathSourceBinder(portal_type='PersonOrInstitution')
        ),
        required=False
    )
    form.widget('printer', SimpleRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')

class IPhysicalDetails(Interface):
    term = schema.TextLine(title=_(u'Physical details'), required=False)

class IAccompanyingMaterial(Interface):
    term = schema.TextLine(title=_(u'Accompanying material'), required=False)

# Series

class ISeries(Interface):
    seriesArticle = schema.TextLine(title=_(u'Series article'), required=False)
    series = schema.TextLine(title=_(u'Series'), required=False)
    seriesNo = schema.TextLine(title=_(u'Series no.'), required=False)
    ISSNSeries = schema.TextLine(title=_(u'ISSN series'), required=False)

class ISubseries(Interface):
    subseriesArticle = schema.TextLine(title=_(u'Subseries article'), required=False)
    subseries = schema.TextLine(title=_(u'Subseries'), required=False)
    subseriesNo = schema.TextLine(title=_(u'Subseries number'), required=False)
    ISSNSubseries = schema.TextLine(title=_(u'ISSN subseries'), required=False)

class IBibliographicalNotes(Interface):
    term = schema.Text(title=_(u'Bibliographical notes'), required=False)

class IISBN(Interface):
    ISBN = schema.TextLine(title=_(u'ISBN'), required=False)
    price = schema.TextLine(title=_(u'Price'), required=False)
    bindingMethod = schema.TextLine(title=_(u'Binding method'), required=False)

class IProduction(Interface):
    term = schema.TextLine(title=_(u'Production'), required=False)

class IBroadcast(Interface):
    term = schema.TextLine(title=_(u'Broadcast'), required=False)

class IBroadcastingCompany(Interface):
    broadcastingCompany = RelationList(
        title=_(u'Broadcasting company'),
        default=[],
        missing_value=[],
        value_type=RelationChoice(
            title=u"Related",
            source=ObjPathSourceBinder(portal_type='PersonOrInstitution')
        ),
        required=False
    )
    form.widget('broadcastingCompany', SimpleRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')

class IProductionCompany(Interface):
    productionCompany = RelationList(
        title=_(u'Production company'),
        default=[],
        missing_value=[],
        value_type=RelationChoice(
            title=u"Related",
            source=ObjPathSourceBinder(portal_type='PersonOrInstitution')
        ),
        required=False
    )
    form.widget('productionCompany', SimpleRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')

class IConference(Interface):
    term = schema.TextLine(title=_(u'Conference'), required=False)



class IMaterialType(Interface):
    term = schema.TextLine(title=_(u'Material type'), required=False)

class IBiblForm(Interface):
    term = schema.TextLine(title=_(u'Bibl. form'), required=False)

class ILanguage(Interface):
    term = schema.TextLine(title=_(u'Language'), required=False)

class INotes(Interface):
    note = schema.Text(title=_(u'Notes'), required=False)

class IAbstractNotes(Interface):
    note = schema.Text(title=_(u'label_notes_op'), required=False)


class IClassNumber(Interface):
    term = schema.TextLine(title=_(u'Class number'), required=False)

class ISubjectTerm(Interface):
    subjectTermType = schema.Choice(title=_(u'Subject term type'), required=True, vocabulary="collective.bibliotheek.subjectermtype", default="No value",  missing_value=" ")
    subjectType = schema.List(
        title=_(u'Subject term'),
        required=False,
        value_type=schema.TextLine(),
        missing_value=[],
        default=[]
    )
    form.widget('subjectType', AjaxSingleSelectFieldWidget, vocabulary="collective.bibliotheek.subjecttype")

    properName = schema.List(
        title=_(u'Proper name'),
        required=False,
        value_type=schema.TextLine(),
        missing_value=[],
        default=[]
    )
    form.widget('properName', AjaxSingleSelectFieldWidget, vocabulary="collective.bibliotheek.propername")

class IPersonKeywordType(Interface):
    personKeywordType = schema.Choice(title=_(u'Person keyword type'), required=True, vocabulary="collective.bibliotheek.personkeywordtype", default="No value",  missing_value=" ")
    name = RelationList(
        title=_(u'Name'),
        default=[],
        missing_value=[],
        value_type=RelationChoice(
            title=u"Related",
            source=ObjPathSourceBinder(portal_type='PersonOrInstitution')
        ),
        required=False
    )
    form.widget('name', SimpleRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')

    role = schema.List(
        title=_(u'Role'),
        required=False,
        value_type=schema.TextLine(),
        missing_value=[],
        default=[]
    )
    form.widget('role', AjaxSingleSelectFieldWidget, vocabulary="collective.bibliotheek.role")

class IGeographicalKeyword(Interface):
    term = schema.TextLine(title=_(u'Geographical keyword'), required=False)

class IPeriod(Interface):
    term = schema.TextLine(title=_(u'Period'), required=False)

class IDigitalReferences(Interface):
    reference = schema.TextLine(title=_(u'Reference'), required=False)

class IAbstract(Interface):
    term = schema.TextLine(title=_(u'Abstract'), required=False)

# Reproductions
class IReproduction(Interface):
    reference = schema.TextLine(title=_(u'Reference'), required=False)
    #type = schema.TextLine(title=_(u'Type'), required=False)
    #format = schema.TextLine(title=_(u'Format'), required=False)
    #date = schema.TextLine(title=_(u'Date'), required=False)
    identifierURL = schema.TextLine(title=_(u'Identifier (URL)'), required=False)
    notes = schema.Text(title=_(u'Notes'), required=False)

##
## Exhibitions, auctions, collections
##
class IExhibition(Interface):
    exhibitionName = RelationList(
        title=_(u'Exhibition name'),
        default=[],
        value_type=RelationChoice(
            title=u"Related",
            source=ObjPathSourceBinder(portal_type="Exhibition")
        ),
        required=False
    )
    form.widget('exhibitionName', SimpleRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')

    #date = schema.TextLine(title=_(u'Date'), required=False)
    #to = schema.TextLine(title=_(u'to'), required=False)
    #organiser = schema.TextLine(title=_(u'Organiser'), required=False)
    #venue = schema.TextLine(title=_(u'Venue'), required=False)
    #place = schema.TextLine(title=_(u'Place'), required=False)
    notes = schema.Text(title=_(u'Notes'), required=False)
    #priref = schema.TextLine(title=_(u'priref'), required=False)


class IAuction(Interface):
    auctionName = schema.TextLine(title=_(u'Auction name'), required=False)
    #auctioneer = schema.TextLine(title=_(u'Auctioneer'), required=False)
    #date = schema.TextLine(title=_(u'Date'), required=False)
    #to = schema.TextLine(title=_(u'to'), required=False)
    #place = schema.TextLine(title=_(u'Place'), required=False)
    #location = schema.TextLine(title=_(u'Location'), required=False)
    #collector = schema.TextLine(title=_(u'Collector'), required=False)
    #commissairPriseur = schema.TextLine(title=_(u'Commissair-priseur'), required=False)
    #auctionNumber = schema.TextLine(title=_(u'Auction number'), required=False)
    notes = schema.Text(title=_(u'Notes'), required=False)

class ICollection(Interface):
    collectionName = schema.TextLine(title=_(u'Collection name'), required=False)
    #collector = schema.TextLine(title=_(u'Collector'), required=False)
    #organisation = schema.TextLine(title=_(u'Organisation'), required=False)
    #date = schema.TextLine(title=_(u'Date'), required=False)
    #place = schema.TextLine(title=_(u'Place'), required=False)
    notes = schema.Text(title=_(u'Notes'), required=False)


# Relations
class IPartOf(Interface):
    partOf = RelationList(
        title=_(u'Part of'),
        default=[],
        value_type=RelationChoice(
            title=u"Related",
            source=ObjPathSourceBinder()
        ),
        required=False
    )
    form.widget('partOf', SimpleRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')

class IConsistsOf(Interface):
    consistsOf = RelationList(
        title=_(u'Consists of'),
        default=[],
        value_type=RelationChoice(
            title=u"Related",
            source=ObjPathSourceBinder()
        ),
        required=False
    )
    form.widget('consistsOf', SimpleRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')

class IMuseumObjects(Interface):
    objectNo = RelationList(
        title=_(u'Object no.'),
        default=[],
        value_type=RelationChoice(
            title=u"Related",
            source=ObjPathSourceBinder(portal_type="Object")
        ),
        required=False
    )
    form.widget('objectNo', SimpleRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')
    #objectName = schema.TextLine(title=_(u'Object name'), required=False)
    #title = schema.TextLine(title=_(u'Title'), required=False)
    #maker = schema.TextLine(title=_(u'Maker'), required=False)

# Free fields
class IFreeFields(Interface):
    date = schema.TextLine(title=_(u'Date'), required=False)
    type = schema.TextLine(title=_(u'Type'), required=False)
    confidential = schema.Bool(title=_(u'Confidential'), required=False, default=False)
    contents = schema.TextLine(title=_(u'Contents'), required=False)


class IOtherNumber(Interface):
    type = schema.TextLine(title=_(u'Type'), required=False)
    contents = schema.TextLine(title=_(u'Contents'), required=False)


class ICopyDetails(Interface):
    copyNumber = schema.TextLine(title=_(u'Copy number'), required=False)
    shelfMark = schema.TextLine(title=_(u'Shelf mark'), required=False)
    
    #availability = schema.TextLine(title=_(u'Availability'), required=False)
    
    loanCategory = schema.List(
        title=_(u'Loan category'),
        required=False,
        value_type=schema.TextLine(),
        missing_value=[],
        default=[]
    )
    form.widget('loanCategory', AjaxSingleSelectFieldWidget, vocabulary="collective.bibliotheek.loanCategory")

    site = schema.List(
        title=_(u'Site'),
        required=False,
        value_type=schema.TextLine(),
        missing_value=[],
        default=[]
    )
    form.widget('site', AjaxSingleSelectFieldWidget, vocabulary="collective.bibliotheek.site")
    locationNotes = schema.Text(title=_(u'Location notes'), required=False)


