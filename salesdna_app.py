import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import io

# Define the five base pairs
base_pairs = [
    "ICP ↔ Value Proposition",
    "Channels ↔ ICP Behavior",
    "Processes ↔ Buying Journey",
    "Tools ↔ Efficiency",
    "Team ↔ Execution Capability"
]

# Benchmarks from the post (for Series A)
benchmarks = {
    "ICP messaging fit": "70%+ is still considered strong",
    "Funnel conversion from awareness to consideration": "15-25% for most SaaS segments",
    "CRM adoption rates for early sales teams": "75%+",
    "CAC payback period": "12-15 months or less",
    "Net dollar retention": "111%+",
    "Average sales cycle": "84 days"
}

# Improvement suggestions based on base pairs
improvement_suggestions = {
    "ICP ↔ Value Proposition": [
        "Refine your Ideal Customer Profile (ICP) by conducting more customer interviews to identify urgent pains.",
        "Update your messaging to explicitly address the ICP's pain points in at least 70% of your content.",
        "Revise your homepage and marketing materials to clearly communicate who you serve, what you offer, and why now."
    ],
    "Channels ↔ ICP Behavior": [
        "Research and prioritize the top 2-3 channels where your ICP spends time, and allocate 80%+ of your budget there.",
        "Implement tracking for lead sources, engagement, and cost per qualified opportunity in each channel.",
        "Develop at least one scalable, non-founder-dependent channel with CAC below your target."
    ],
    "Processes ↔ Buying Journey": [
        "Map out your ICP's buying journey in detail through customer feedback and data analysis.",
        "Align content, CTAs, and touchpoints to each stage of the buying journey to reduce drop-offs.",
        "Document your sales processes to make them repeatable across the team."
    ],
    "Tools ↔ Efficiency": [
        "Integrate your CRM, marketing automation, and analytics tools for seamless data flow.",
        "Automate repetitive tasks like follow-up emails to free up team time.",
        "Move away from manual spreadsheets by setting up automated tracking for key metrics."
    ],
    "Team ↔ Execution Capability": [
        "Create a comprehensive GTM playbook that all sales and marketing team members follow.",
        "Define clear KPIs focused on ICP conversion, track them weekly, and avoid vanity metrics.",
        "Hire or consult a GTM leader with experience scaling beyond your current stage."
    ]
}

def display_checklist():
    st.markdown("### DIY Diagnostic Checklist")
    
    st.markdown("**ICP ↔ Value Proposition:**")
    st.markdown("- Have you defined a single, narrow ICP (industry, size, role, urgent pain)?")
    st.markdown("- Does 70%+ of your messaging explicitly speak to that pain?")
    st.markdown("- Can a stranger read your homepage and immediately understand the who, what, and why now?")
    
    st.markdown("**Channels ↔ ICP Behavior:**")
    st.markdown("- Are you investing 80%+ of your budget/time into the 2 channels where your ICP already is?")
    st.markdown("- Are you measuring lead source, engagement, and cost per qualified opportunity by channel?")
    st.markdown("- For Series A founders: Do you have at least one non-founder dependent channel showing consistent CAC below your target?")
    
    st.markdown("**Processes ↔ Buying Journey:**")
    st.markdown("- Have you mapped your ICP's actual buying journey (trigger → discovery → evaluation → decision)?")
    st.markdown("- Are you matching content, CTAs, and touchpoints to each stage?")
    st.markdown("- For Series A+ companies: Is your process documented and repeatable across team members?")
    
    st.markdown("**Tools ↔ Efficiency:**")
    st.markdown("- Are your CRM, marketing automation, and analytics systems integrated and actively used?")
    st.markdown("- Are repetitive tasks (e.g., follow-up emails) automated?")
    st.markdown("- For Series A founders: Can you track pipeline, conversion, and revenue metrics without manual spreadsheets?")
    
    st.markdown("**Team ↔ Execution Capability:**")
    st.markdown("- Is there a defined GTM playbook every sales/marketing person follows?")
    st.markdown("- Are KPIs clear, tracked weekly, and tied to ICP conversion, not vanity metrics?")
    st.markdown("- For Series A founders: Do you have at least one GTM leader who has scaled past your current stage?")
    
    st.markdown("Use this checklist to guide your scoring.")

def get_user_scores():
    scores = []
    st.markdown("### Enter Your Scores")
    st.write("For each base pair, score yourself on a 1-10 scale (1 being poor, 10 being excellent). Be honest based on the criteria provided in the framework.")
    
    for bp in base_pairs:
        score = st.slider(f"Score for {bp}", min_value=1, max_value=10, value=5)
        scores.append(score)
    
    return scores

def calculate_average(scores):
    return sum(scores) / len(scores)

def display_results(scores, average):
    st.markdown("### Your SalesDNA Scores")
    for bp, score in zip(base_pairs, scores):
        st.write(f"{bp}: {score}/10")
    
    st.write(f"**Average Score:** {average:.2f}/10")
    
    if average >= 8:
        st.success("Strong shape = ready to scale. Your GTM is in good health!")
    elif average >= 5:
        st.warning("Moderate shape. Identify weak areas and improve before scaling.")
    else:
        st.error("Weak shape = fix before you spend more. Focus on foundational alignments.")

def generate_summary(scores, average):
    st.markdown("### Personalized Results Summary and Action Plan")
    
    if average >= 8:
        st.write("**Overall Assessment:** Your SalesDNA is strong and well-aligned. You're in a great position to scale your GTM efforts sustainably. Focus on maintaining this balance while monitoring for any emerging misalignments.")
    elif average >= 5:
        st.write("**Overall Assessment:** Your GTM strategy has solid foundations but shows some imbalances. Addressing the weaker areas will help you achieve more consistent revenue growth and better prepare for funding challenges.")
    else:
        st.write("**Overall Assessment:** Your SalesDNA indicates significant misalignments that could hinder growth and lead to inefficient resource use. Prioritize foundational fixes to avoid burning runway on ineffective tactics.")
    
    st.write("**Key Insights from Your Scores:**")
    low_scores = [bp for bp, score in zip(base_pairs, scores) if score < 6]
    if low_scores:
        st.write(f"You have lower scores in: {', '.join(low_scores)}. These are critical areas to address first, as they form the base of your GTM health.")
    else:
        st.write("All areas are relatively strong, but continue iterating for optimization.")
    
    high_scores = [bp for bp, score in zip(base_pairs, scores) if score >= 8]
    if high_scores:
        st.write(f"Strengths include: {', '.join(high_scores)}. Leverage these to support improvements in weaker areas.")
    
    st.write("**Recommended Actions:**")
    st.write("Based on your scores, here are prioritized steps to improve. Focus on areas below 6 first:")
    for bp, score in zip(base_pairs, scores):
        if score < 6:
            st.markdown(f"**{bp} (Score: {score}/10) - High Priority:**")
            for suggestion in improvement_suggestions[bp]:
                st.write(f"- {suggestion}")
        elif score < 8:
            st.markdown(f"**{bp} (Score: {score}/10) - Medium Priority:**")
            for suggestion in improvement_suggestions[bp][:2]:  # Limit to top 2 for medium
                st.write(f"- {suggestion}")
        else:
            st.markdown(f"**{bp} (Score: {score}/10) - Low Priority:** Maintain current efforts.")

    st.write("Re-run this diagnostic after implementing changes and running experiments to track progress.")

def display_benchmarks():
    st.markdown("### Industry Benchmarks for Series A (from the framework)")
    for key, value in benchmarks.items():
        st.write(f"- {key}: {value}")

def plot_radar_chart(scores):
    num_vars = len(base_pairs)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]
    scores += scores[:1]
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, scores, color='blue', alpha=0.25)
    ax.plot(angles, scores, color='blue', linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(base_pairs, fontsize=10)
    ax.set_title("Your SalesDNA Radar Chart")
    
    # Save to buffer
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return buf

def run_evaluation_process():
    st.markdown("### How to Run Your Own SalesDNA Evaluation")
    
    st.markdown("1. **Evaluate Each Base Pair Ruthlessly**")
    st.markdown("   - Collect concrete data through:")
    st.markdown("     - Customer interviews (minimum 5, structured around buying journey)")
    st.markdown("     - Sales call recordings (minimum 10, analyzed for objections)")
    st.markdown("     - Marketing analytics (channel performance, engagement metrics)")
    st.markdown("     - CRM data (conversion rates, deal velocities, drop-off points)")
    st.markdown("   - Score each base pair on the 1-10 scale with honesty.")
    
    st.markdown("2. **Benchmark Against Industry Standards (Series A)**")
    display_benchmarks()
    
    st.markdown("3. **Visualize Your SalesDNA**")
    st.markdown("   - Plot your scores on a radar chart (displayed below).")
    st.markdown("   - Goal: Balanced, expanding shape — not collapsed or uneven.")
    
    st.markdown("4. **Build a Hypothesis → Test → Measure Loop**")
    st.markdown("   - Hypothesize: e.g., 'Narrowing ICP to HR managers will 2x lead quality'")
    st.markdown("   - Test: Run targeted campaigns for 2-4 weeks")
    st.markdown("   - Measure: Track lead quality, conversion rates")
    st.markdown("   - Iterate: Double down or pivot based on results")
    st.markdown("   - Run this cycle weekly for exponential GTM learning.")

# Main Streamlit app
def main():
    st.title("SalesDNA Diagnostic Tool")
    st.write("Welcome! This tool helps you diagnose and improve your Go-To-Market (GTM) strategy using the SalesDNA Framework.")
    
    display_checklist()
    
    scores = get_user_scores()
    
    if st.button("Calculate Results"):
        average = calculate_average(scores)
        display_results(scores, average)
        
        # Generate and display personalized summary
        generate_summary(scores, average)
        
        # Display radar chart
        chart_buf = plot_radar_chart(scores)
        st.image(chart_buf, caption="Your SalesDNA Radar Chart", use_container_width=True)
        
        run_evaluation_process()
        
        st.markdown("### Final Note")
        st.write("Use this tool regularly to monitor and improve your GTM strategy. In today's funding environment, GTM efficiency is key to survival.")

if __name__ == "__main__":
    main()
