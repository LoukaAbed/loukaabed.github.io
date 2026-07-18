import streamlit as st
import utils.ui as ui

left, center, right =st.columns(3)
with center:
    st.title("Louka Abed")
st.subheader("Clinical Data Scientist | AI Translational Medicine & Pharma R&D")
st.write("""International Medical Graduate (MD) combining clinical and biochemistry domain expertise with MS in Data Science and Mathematics foundations to validate, 
audit, model, and extract AI insights—accelerating novel drug discovery and building predictive translational medicine pipelines through a systems approach 
that integrates complex healthcare data streams, high-throughput genomic and proteomic registries, and heterogeneous multiomics architectures.""")


st.write("**Employment Status:** US Citizen | Fully authorized for US employment with no sponsorship required.")

st.divider()
st.markdown("### Technical & Mathematical Skills")
st.write("""
* **Programming & Scripting:** Python (Pandas/Core syntax), SQL database querying, R, Java, MATLAB, Microsoft Excel.
* **Quantitative Analytics Core:** Linear Algebra, Calculus, Differential Equations, Probability & Statistical concepts.
* **Enterprise Platforms & Systems:** Electronic Health Records (EHR), SAP, Syncade, Sequencher, Automated Liquid-Handling Robotics.
""")

st.divider()

st.markdown("### Education")

st.markdown("**MS in Data Science** | Eastern University | Expected Graduation: May 2027 (In Progress)")
st.write("* *Completed Foundations:* Principles of Python Programming, Data and Database Management with SQL.")

st.markdown("**Bachelor of Medicine, Bachelor of Surgery (M.B. B.Ch. / MD Equivalent)** | Cairo University Faculty of Medicine")
st.write("* *Clinical Clerkships:* Columbia University College of Physicians and Surgeons (NY). Utilized electronic clinical databases; passed USMLE Step 1.")

st.markdown("**BS in Biochemistry (Mathematics Minor)** | University of Massachusetts, Boston")
st.write("* *Honors & Awards:* Summa Cum Laude, GPA: 3.86/4.00, Emil Fischer Book Award.")

st.divider()

st.markdown("### Systems, Data, & Clinical Operations Experience")

st.markdown("**Technical Operations Associate (Personalized Vaccine Unit)** | Moderna | 04/2023 – 03/2025")
st.write("""
* Managed digital workflows and production metrics within automated GMP oncology manufacturing pipelines.
* Utilized enterprise software frameworks including SAP, Syncade, and Sequencher to maintain strict quality control and data integrity across technical runs.
""")

st.markdown("**Clinical Operations & Case Management** | Ministry of Health / Teaching Hospitals | 03/2019 – 02/2023")
st.write("""
* Maintained, audited, and updated diagnostic registries and patient health databases across primary care and emergency departments.
* Ensured data compliance with healthcare protocols while documenting multi-department clinical cases.
""")

st.markdown("**Medical Data Analyst** | Innodata – Synodex Division | 11/2015 – 03/2016")
st.write("""
* Conducted systematic medical literature reviews to isolate, track, and document evidence-based risk metrics.
* Applied advanced Excel formatting and text sorting arrays to process high-volume liability assessment data.
""")

st.markdown("**Technical Research Associate** | Columbia University Medical Center | 06/2012 – 12/2013")
st.write("""
* Executed high-precision laboratory assays and extracted mRNA targets for genetic sequencing pipelines within the Systems Biology and Nephrology divisions.
* Leveraged digital genomic registries including the UCSC Genome Browser and dbSNP data frameworks to validate structural variations.
""")

st.markdown("**Process Development Associate** | Broad Institute | 01/2011 – 04/2011")
st.write("""
* Programmed and operated Multiprobe automated liquid-handling robotics for high-throughput microbial genomic sequencing data generation workflows.
""")

st.divider()

st.markdown("### Publications")
st.write('Kyriakakis, P., Tipping, M., **Abed, L.**, Veraksa, A. "Tandem affinity purification in Drosophila: The advantages of the GS-TAP system." *Fly*, 2:229-235.')

st.divider()

st.divider()
ui.message()