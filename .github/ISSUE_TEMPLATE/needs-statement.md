---
name: "Needs Statement"
about: "Neuen Bedarf oder eine Idee beschreiben. Dieses Issue ist der Startpunkt für spec-mode."
title: "[NEEDS] "
labels: ["needs-statement", "needs-spec"]
assignees: ''
---

<!--
INTERVIEW-LEITFADEN
═══════════════════
Dieses Template kann direkt als Gesprächsleitfaden im Kundengespräch verwendet werden.
Die kursiven Hinweise unter den Abschnitten sind Interviewfragen – sie werden im fertigen
Issue nicht angezeigt. Fülle die Checkboxen aus während du das Gespräch führst.

Wichtig: Keine UIDs, keine Spec-IDs hier eintragen – das macht spec-agent.
-->

---

## 1 – Problem / Ausgangssituation

*Interviewfrage: „Was passiert heute, das nicht passieren sollte – oder was fehlt ganz?"*
*Ziel: Symptom beschreiben, nicht die Lösung.*

> **Situation:**

> **Konsequenz wenn ungelöst:**

- [ ] Problem aus Nutzerperspektive beschrieben (nicht technisch)

---

## 2 – Betroffene Nutzer / Stakeholder

*Interviewfrage: „Wer ist davon direkt betroffen? Wer merkt es zuerst?"*

| Rolle / Persona | Betroffenheit |
|-----------------|---------------|
|                 |               |

---

## 3 – Gewünschtes Ergebnis

*Interviewfrage: „Was soll nach der Umsetzung möglich sein, das heute nicht möglich ist?"*
*Ziel: Ergebnis beschreiben – nicht wie es gebaut wird.*

- Vorher: 
- Nachher: 

- [ ] Ergebnis aus Nutzersicht formuliert (kein „wir brauchen eine API...")

---

## 4 – Randbedingungen & Einschränkungen

*Interviewfrage: „Was darf auf keinen Fall passieren? Gibt es gesetzliche oder technische Grenzen?"*

| Typ | Beschreibung |
|-----|-------------|
| Pflicht |  |
| Verboten |  |
| Offen / unklar |  |

---

## 5 – Abgrenzung – explizit NICHT im Scope

*Interviewfrage: „Was könnte man verwechseln? Was soll bewusst NICHT umgesetzt werden?"*

- 

- [ ] Abgrenzung explizit benannt

---

## 6 – Akzeptanzvorstellung

*Interviewfrage: „Woran würdest du erkennen, dass es fertig und richtig ist? Kannst du es mir zeigen?"*
*Das sind informelle ACs – spec-agent formalisiert sie später.*

- [ ] 
- [ ] 
- [ ] 

---

## 7 – Priorität / Dringlichkeit

*Interviewfrage: „Wenn wir das in 3 Monaten noch nicht haben – was passiert dann?"*

- [ ] Kritisch – Blocker (Betrieb nicht möglich)
- [ ] Hoch – nächster Sprint
- [ ] Mittel – geplant, kein Zeitdruck
- [ ] Niedrig – Nice-to-have

---

## 8 – Offene Fragen vor der Spec

*Was muss noch geklärt werden, bevor spec-agent loslegen kann?*

- [ ] 

---

> **Nächster Schritt:** @spec-agent konvertiert dieses Issue in formale Spec-Nodes mit UID.
> Spec-IDs und Subsystem-Codes werden durch spec-agent vergeben – hier keine IDs eintragen.
