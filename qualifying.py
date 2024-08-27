import streamlit as st
def show_notes(disease):
    notes = {
        "Multiple myeloma": "A type of cancer that forms in plasma cells, which are a type of white blood cell. It often affects the bones, causing pain, fractures, and bone lesions.",
        "Langerhans Cell Histiocytosis": "A rare disease involving the proliferation of Langerhans cells, which are a type of immune cell. It can cause bone lesions, among other symptoms.",
        "Leukemia/lymphoma": "Blood cancers that can involve the bone marrow and cause various types of bone lesions.",
        "Metastatic diseases": "Cancers that have spread from their original site to the bone, causing lesions.",
        "Squamous odontogenic tumor": "A rare benign odontogenic tumor that can cause lesions in the jawbone.",
        "Multiple Keratocysts": "Cysts that occur in the jawbone, often associated with genetic syndromes like Gorlin syndrome.",
        "Cherubism (bilateral)": "A genetic disorder that causes bilateral swelling of the jawbones in children.",
        "Paget’s disease of bone": "A chronic bone disorder that can cause enlarged and weakened bones, leading to deformities and pain.",
        "Central Giant Cell Granuloma": "A benign bone lesion that can cause swelling and bone destruction.",
        "Hyperparathyroidism": "A condition characterized by overactivity of the parathyroid glands, which can lead to bone changes and lesions.",
        "Osseous Dysplasia": "A condition involving abnormal bone development, which can lead to lesions in the jawbone.",
        "Gorham-Stout Disease": "A rare bone disorder that causes progressive bone loss and can lead to large bone lesions.",
        "Osteomyelitis": "An infection of the bone that can cause pain, swelling, and bone destruction.",
        "Periapical granuloma": "A type of granuloma that forms at the apex of a tooth root, often due to infection.",
        "Radicular cyst": "A cyst that forms at the root of a tooth, often as a result of chronic pulpitis.",
        "Other benign odontogenic cysts or tumors": "Includes various benign lesions originating from tooth-forming tissues.",
        "Early stage of osseous dysplasia": "A condition characterized by abnormal bone development, often presenting in early stages.",
        "Early stage of ossifying fibroma": "A benign tumor of the bone that begins with fibrous tissue and can evolve over time.",
        "Dentigerous cyst": "A type of odontogenic cyst associated with the crown of an unerupted tooth.",
        "Unicystic ameloblastoma": "A type of ameloblastoma that presents as a single cystic lesion.",
        "Keratocyst": "An odontogenic cyst characterized by a unique lining and aggressive behavior.",
        "Ameloblastic fibroma": "A benign tumor composed of both dental epithelium and mesenchymal tissue.",
        "Lateral Inflammatory cyst": "An inflammatory cyst that develops along the lateral aspect of the roots of teeth.",
        "Lateral developmental cyst": "A type of developmental cyst located along the lateral aspect of the jawbone.",
        "Traumatic bone cyst": "A cystic bone lesion thought to be related to trauma.",
        "Squamous odontogenic tumor": "A rare odontogenic tumor composed of squamous cells.",
        "Median Palatine cyst": "A developmental cyst located in the midline of the hard palate.",
        "Globulomaxillary cyst": "A cyst located between the roots of the maxillary lateral incisor and canine teeth.",
        "Vascular malformation": "An abnormality in blood vessels that can lead to bone lesions.",
        "Schwannoma": "A tumor of the Schwann cells that can occur in the jawbone.",
        "Neurofibroma": "A benign nerve sheath tumor that can occur in the jawbone.",
        "Static bone cyst": "A benign bone cyst with no active growth or inflammation.",
        "Plasmacytoma": "A solitary plasma cell tumor that can occur in bone or soft tissue.",
        "Paget’s disease": "A chronic bone disorder characterized by abnormal and excessive bone remodeling.",
        "Leukemia/lymphoma": "Blood cancers that can involve the bone marrow and cause various types of bone lesions.",
        "Metastasis": "The spread of cancer from its original site to other parts of the body, including bone.",
        "Chronic periapical abscess": "A localized infection at the apex of a tooth root that persists over time.",
        "Osteomyelitis": "An infection of the bone that can cause pain, swelling, and bone destruction.",
        "Malignant odontogenic tumors": "Cancers arising from the odontogenic tissues with aggressive behavior.",
        "Central Giant Cell Granuloma (CGCG)": "A benign bone lesion characterized by giant cells and central cystic spaces.",
        "Glandular odontogenic cyst": "A cyst with glandular epithelial lining, often found in the jawbone.",
        "Ameloblastoma": "A benign but locally aggressive odontogenic tumor with a potential for recurrence.",
        "Odontogenic keratocyst": "A cystic lesion with a unique lining and high recurrence rate.",
        "Odontogenic myxoma": "A rare, benign tumor of the jaw characterized by a myxoid stroma.",
        "Central odontogenic fibroma": "A benign tumor with fibrous tissue that originates in the jawbone.",
        "Central hemangioma": "A benign vascular tumor located within the jawbone.",
        "Aneurysmal bone cyst": "A benign bone lesion with blood-filled cystic spaces.",
        "Ameloblastic fibroma": "A benign tumor composed of both dental epithelium and mesenchymal tissue."
    }
    st.write(notes.get(disease, "No information available."))

def lesion_diagnosis():
    st.title("Lesion Differential Diagnosis")

    lesion_type = st.selectbox("Select the lesion type:", ["focal", "multifocal"])

    if lesion_type == "multifocal":
        st.write("The lesion differential diagnosis could be:")

        diseases = [
            "Multiple myeloma",
            "Langerhans Cell Histiocytosis",
            "Leukemia/lymphoma",
            "Metastatic diseases",
            "Squamous odontogenic tumor",
            "Multiple Keratocysts",
            "Cherubism (bilateral)",
            "Paget’s disease of bone",
            "Central Giant Cell Granuloma",
            "Hyperparathyroidism",
            "Osseous Dysplasia",
            "Gorham-Stout Disease",
            "Osteomyelitis"
        ]

        for disease in diseases:
            if st.button(disease):
                show_notes(disease)

    elif lesion_type == "focal":
        locularity = st.selectbox("Is the lesion unilocular or multilocular?", ["unilocular", "multilocular"])

        if locularity == "unilocular":
            border = st.selectbox("Is the lesion well defined or ill defined?", ["well defined", "ill defined"])

            if border == "well defined":
                location_type = st.selectbox("Is the lesion tooth-related, has a specific site, or with no specific site?", ["tooth-related", "specific site", "no specific site"])

                if location_type == "tooth-related":
                    tooth_location = st.selectbox("Is the lesion periapical, pericoronal, or interradicular?", ["periapical", "pericoronal", "interradicular"])

                    if tooth_location == "periapical":
                        st.write("The lesion could be:")
                        lesions = [
                            "Periapical granuloma",
                            "Radicular cyst",
                            "Other benign odontogenic cysts or tumors",
                            "Early stage of osseous dysplasia",
                            "Early stage of ossifying fibroma"
                        ]

                        for lesion in lesions:
                            if st.button(lesion):
                                show_notes(lesion)

                    elif tooth_location == "pericoronal":
                        st.write("The lesion could be:")
                        lesions = [
                            "Dentigerous cyst",
                            "Unicystic ameloblastoma",
                            "Keratocyst",
                            "Ameloblastic fibroma"
                        ]

                        for lesion in lesions:
                            if st.button(lesion):
                                show_notes(lesion)

                    elif tooth_location == "interradicular":
                        st.write("The lesion could be:")
                        lesions = [
                            "Lateral Inflammatory cyst",
                            "Lateral developmental cyst",
                            "Traumatic bone cyst",
                            "Squamous odontogenic tumor"
                        ]

                        for lesion in lesions:
                            if st.button(lesion):
                                show_notes(lesion)

                elif location_type == "specific site":
                    site = st.selectbox("Is the lesion in the anterior maxilla, within the inferior alveolar nerve, or below the inferior alveolar nerve?", ["anterior maxilla", "within the inferior alveolar nerve", "below the inferior alveolar nerve"])

                    if site == "anterior maxilla":
                        st.write("The lesion could be:")
                        lesions = [
                            "Median Palatine cyst",
                            "Globulomaxillary cyst"
                        ]

                        for lesion in lesions:
                            if st.button(lesion):
                                show_notes(lesion)

                    elif site == "within the inferior alveolar nerve":
                        st.write("The lesion could be:")
                        lesions = [
                            "Vascular malformation",
                            "Schwannoma",
                            "Neurofibroma"
                        ]

                        for lesion in lesions:
                            if st.button(lesion):
                                show_notes(lesion)

                    elif site == "below the inferior alveolar nerve":
                        st.write("The lesion could be:")
                        lesions = ["Static bone cyst"]

                        for lesion in lesions:
                            if st.button(lesion):
                                show_notes(lesion)

                elif location_type == "no specific site":
                    st.write("The lesion could be:")
                    lesions = [
                        "Plasmacytoma",
                        "Hyperparathyroidism",
                        "Paget’s disease",
                        "Leukemia/lymphoma",
                        "Metastasis"
                    ]

                    for lesion in lesions:
                        if st.button(lesion):
                            show_notes(lesion)

            elif border == "ill defined":
                st.write("The lesion could be:")
                lesions = [
                    "Chronic periapical abscess",
                    "Osteomyelitis",
                    "Malignant odontogenic tumors"
                ]

                for lesion in lesions:
                    if st.button(lesion):
                        show_notes(lesion)

        elif locularity == "multilocular":
            border = st.selectbox("Is the lesion well defined or ill defined?", ["well defined", "ill defined"])

            if border == "ill defined":
                st.write("The lesion could be:")
                lesions = ["Malignant odontogenic tumors"]

                for lesion in lesions:
                    if st.button(lesion):
                        show_notes(lesion)

            elif border == "well defined":
                location = st.selectbox("Is the lesion in the anterior of the jaw or posterior of the jaw?", ["anterior", "posterior"])

                if location == "anterior":
                    st.write("The lesion could be:")
                    lesions = [
                        "Central Giant Cell Granuloma (CGCG)",
                        "Glandular odontogenic cyst"
                    ]

                    for lesion in lesions:
                        if st.button(lesion):
                            show_notes(lesion)

                elif location == "posterior":
                    st.write("The lesion could be:")
                    lesions = [
                        "Ameloblastoma",
                        "Odontogenic keratocyst",
                        "Odontogenic myxoma",
                        "Central odontogenic fibroma",
                        "Central hemangioma",
                        "Aneurysmal bone cyst",
                        "Ameloblastic fibroma"
                    ]

                    for lesion in lesions:
                        if st.button(lesion):
                            show_notes(lesion)

    else:
        st.write("Invalid input. Please specify 'focal' or 'multifocal'.")

# Main function to run the Streamlit app
def main():
    lesion_diagnosis()

if __name__ == "__main__":
    main()
