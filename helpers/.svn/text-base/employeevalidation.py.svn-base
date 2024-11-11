from apps.intent.party.models.Party import Party
from apps.intent.party.models.Partyroletype import Partyroletype
from apps.intent.party.models.Person import Person
from django.shortcuts import render_to_response,  get_object_or_404, redirect

def isemployee(party_id):
    employee=False
    try:
        party=Party.objects.get(id=party_id,party_type_id=1)
        if party:
            partyrole=get_object_or_404(Partyroletype, party_id=party_id,role_type=18)
            if partyrole:
                person=Person.objects.get(party_id=party_id)
                if person:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    except Exception as error:
        return False
